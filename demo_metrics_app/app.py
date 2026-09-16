"""Demo Flask app: exposes PowerStore performance metrics in Prometheus format.

This is a DEMO, not a production monitoring tool. There is no real
PowerStore array behind it - PyPowerStore's MetricsFunctions is driven by
a unittest.mock-based fake connection (see get_mocked_metrics_client()
below), so the numbers this app reports are made up. It exists to show a
real Prometheus /metrics endpoint wired up to Dell's PyPowerStore SDK, for
a DevOps pipeline demo. See demo_metrics_app/README.md for the full
explanation.
"""

from unittest.mock import MagicMock

from flask import Flask, Response, jsonify
from prometheus_client import CONTENT_TYPE_LATEST, Gauge, generate_latest

from PyPowerStore.metrics import MetricsFunctions

app = Flask(__name__)

CPU_USAGE = Gauge(
    "powerstore_appliance_cpu_usage_percent",
    "Mocked PowerStore appliance CPU usage percentage",
    ["entity_id"],
)
MEMORY_USAGE = Gauge(
    "powerstore_appliance_memory_usage_percent",
    "Mocked PowerStore appliance memory usage percentage",
    ["entity_id"],
)
DISK_USAGE = Gauge(
    "powerstore_appliance_disk_usage_percent",
    "Mocked PowerStore appliance disk usage percentage",
    ["entity_id"],
)


def get_mocked_metrics_client():
    """Build a MetricsFunctions instance backed by a mocked connection.

    provisioning.client (the REST client PyPowerStore normally sends real
    HTTP requests to a PowerStore array through) is replaced with a
    unittest.mock.MagicMock whose .request() call returns a canned
    response shaped like a real PowerStore API reply. This lets
    get_performance_metrics() run its real code path without a network
    call or array credentials.
    """
    mock_provisioning = MagicMock()
    mock_provisioning.server_ip = "mocked-powerstore.example.com"
    mock_provisioning.client.request.return_value = {
        "metrics": [
            {
                "timestamp": "2024-01-01T00:00:00Z",
                "entity_id": "A1",
                "entity_type": "appliance",
                "values": {
                    "cpu_usage": 42.5,
                    "memory_usage": 61.2,
                    "disk_usage": 33.8,
                },
            },
        ],
    }
    return MetricsFunctions(mock_provisioning)


@app.route("/health")
def health():
    """Basic liveness check for the container/orchestrator."""
    return jsonify(status="ok"), 200


@app.route("/metrics")
def metrics():
    """Fetch mocked PowerStore performance metrics, expose them as Prometheus metrics."""
    client = get_mocked_metrics_client()
    response = client.get_performance_metrics(
        entity="performance_metrics_by_appliance",
        entity_id="A1",
        interval="Five_Sec",
    )

    for entry in response.get("metrics", []):
        entity_id = entry.get("entity_id", "unknown")
        values = entry.get("values", {})
        CPU_USAGE.labels(entity_id=entity_id).set(values.get("cpu_usage", 0))
        MEMORY_USAGE.labels(entity_id=entity_id).set(values.get("memory_usage", 0))
        DISK_USAGE.labels(entity_id=entity_id).set(values.get("disk_usage", 0))

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
