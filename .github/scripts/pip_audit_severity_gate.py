#!/usr/bin/env python3
"""Run pip-audit and fail the build only for HIGH/CRITICAL severity findings.

pip-audit (checked: v2.9.0 --help) has no built-in severity threshold, so
"fail on any finding" and "fail on high severity" are not the same thing.
This script runs pip-audit to discover vulnerability IDs for the pinned
requirements, then asks the OSV.dev API for each finding's severity and
only fails the job on HIGH/CRITICAL results. LOW/MODERATE findings are
printed so they're visible in the CI log, but do not fail the build.
"""

import json
import math
import re
import subprocess
import sys
import urllib.request

HIGH_SEVERITY_LABELS = {"HIGH", "CRITICAL"}
HIGH_CVSS_THRESHOLD = 7.0

CVSS_V3_WEIGHTS = {
    "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
    "AC": {"L": 0.77, "H": 0.44},
    "PR": {"N": 0.85, "L": 0.62, "H": 0.27},
    "PR_C": {"N": 0.85, "L": 0.68, "H": 0.5},
    "UI": {"N": 0.85, "R": 0.62},
    "CIA": {"N": 0.0, "L": 0.22, "H": 0.56},
}


def run_pip_audit(requirements_file):
    result = subprocess.run(
        ["pip-audit", "-r", requirements_file, "-f", "json", "--desc", "off"],
        capture_output=True,
        text=True,
    )
    if result.returncode not in (0, 1):
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        sys.exit(f"pip-audit failed to run (exit {result.returncode})")
    return json.loads(result.stdout)


def cvss_v3_base_score(vector):
    """Compute the CVSS v3.1 base score from a vector string. Returns None
    if the vector can't be parsed (e.g. it's a CVSS v2 vector)."""
    if not vector or "CVSS:3" not in vector:
        return None
    metrics = dict(part.split(":") for part in vector.split("/") if ":" in part)
    try:
        scope_changed = metrics["S"] == "C"
        av = CVSS_V3_WEIGHTS["AV"][metrics["AV"]]
        ac = CVSS_V3_WEIGHTS["AC"][metrics["AC"]]
        pr = CVSS_V3_WEIGHTS["PR_C" if scope_changed else "PR"][metrics["PR"]]
        ui = CVSS_V3_WEIGHTS["UI"][metrics["UI"]]
        c = CVSS_V3_WEIGHTS["CIA"][metrics["C"]]
        i = CVSS_V3_WEIGHTS["CIA"][metrics["I"]]
        a = CVSS_V3_WEIGHTS["CIA"][metrics["A"]]
    except KeyError:
        return None

    isc_base = 1 - ((1 - c) * (1 - i) * (1 - a))
    if scope_changed:
        impact = 7.52 * (isc_base - 0.029) - 3.25 * (isc_base - 0.02) ** 15
    else:
        impact = 6.42 * isc_base
    if impact <= 0:
        return 0.0

    exploitability = 8.22 * av * ac * pr * ui
    base = (impact + exploitability) * (1.08 if scope_changed else 1)
    base = min(base, 10)
    return math.ceil(base * 10) / 10


def severity_of(vuln_id):
    """Return (label, source) for a vulnerability ID, using OSV.dev's
    GitHub-assigned label when available, else a CVSS v3 base score."""
    url = f"https://api.osv.dev/v1/vulns/{vuln_id}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
    except Exception as exc:
        print(f"  warning: could not fetch severity for {vuln_id}: {exc}")
        return "UNKNOWN", "lookup failed"

    label = data.get("database_specific", {}).get("severity")
    if label:
        return label, "GitHub advisory rating"

    for entry in data.get("severity", []):
        if entry.get("type") == "CVSS_V3":
            score = cvss_v3_base_score(entry.get("score"))
            if score is not None:
                if score >= 9.0:
                    return "CRITICAL", f"CVSS v3 base score {score}"
                if score >= HIGH_CVSS_THRESHOLD:
                    return "HIGH", f"CVSS v3 base score {score}"
                return "MODERATE", f"CVSS v3 base score {score}"

    return "UNKNOWN", "no severity data available"


def main():
    requirements_file = sys.argv[1] if len(sys.argv) > 1 else "requirements.txt"
    audit = run_pip_audit(requirements_file)

    findings = []
    for dep in audit.get("dependencies", []):
        for vuln in dep.get("vulns", []):
            label, source = severity_of(vuln["id"])
            findings.append((dep["name"], dep["version"], vuln["id"], label, source))

    if not findings:
        print("pip-audit: no known vulnerabilities found in", requirements_file)
        return

    print(f"pip-audit findings in {requirements_file}:")
    high = []
    for name, version, vuln_id, label, source in findings:
        print(f"  {name}=={version}: {vuln_id} - severity {label} ({source})")
        if label in HIGH_SEVERITY_LABELS:
            high.append((name, version, vuln_id, label))

    if high:
        print(f"\n{len(high)} HIGH/CRITICAL severity issue(s) found - failing build:")
        for name, version, vuln_id, label in high:
            print(f"  {name}=={version}: {vuln_id} ({label})")
        sys.exit(1)

    print("\nNo HIGH or CRITICAL severity issues found - lower-severity findings above do not fail the build.")


if __name__ == "__main__":
    main()
