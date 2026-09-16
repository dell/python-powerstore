# Build from the repo root, e.g.:
#   docker build -f demo_metrics_app/Dockerfile -t demo-metrics-app .
# (This app imports PyPowerStore, so the build context has to be the
# whole repo, not just demo_metrics_app/.)

FROM python:3.12-slim

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
