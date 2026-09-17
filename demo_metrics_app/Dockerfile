# Build from the repo root, e.g.:
#   docker build -f demo_metrics_app/Dockerfile -t demo-metrics-app .
# (This app imports PyPowerStore, so the build context has to be the
# whole repo, not just demo_metrics_app/.)

FROM python:3.12-slim

# Pick up whatever OS-level security patches Debian has published since
# this base image was built (perl, libsqlite3, libpcre2, etc.) - the
# demo-pipeline.yml Trivy scan flags these even though they're not our
# code, so keep them current here rather than ignoring them.
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install PyPowerStore itself first - Dell's SDK this demo app builds on.
COPY setup.py .
COPY PyPowerStore/ ./PyPowerStore/
RUN pip install --no-cache-dir .

# Then install and add the demo app.
COPY demo_metrics_app/requirements.txt demo_metrics_app/requirements.txt
RUN pip install --no-cache-dir -r demo_metrics_app/requirements.txt
COPY demo_metrics_app/app.py demo_metrics_app/app.py

EXPOSE 5000

CMD ["python", "demo_metrics_app/app.py"]
