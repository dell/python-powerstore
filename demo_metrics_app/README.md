# demo_metrics_app

A small Flask app, two routes:

- `/health` returns `{"status": "ok"}` — used as the k8s liveness/readiness
  check
- `/metrics` calls PyPowerStore's real `get_performance_metrics()` function
  and re-exposes whatever it returns in Prometheus text format

The metrics are fake. I don't have a real PowerStore array to point this
at, so `/metrics` runs against a mocked connection (`unittest.mock`)
that hands back made-up CPU/memory/disk numbers, shaped like a real
array's response. The SDK call itself isn't touched or simplified — only
the network layer underneath it is faked. Swap the mock for a real
connection and credentials and the same code path would return real
numbers.

## Running it

Flask app on its own:

```bash
pip install -e .
pip install -r demo_metrics_app/requirements.txt
python demo_metrics_app/app.py
```

Docker:

```bash
docker build -f demo_metrics_app/Dockerfile -t demo-metrics-app .
docker run -p 5000:5000 demo-metrics-app
```

Minikube:

```bash
minikube start
eval $(minikube docker-env)
docker build -f demo_metrics_app/Dockerfile -t demo-metrics-app:latest .
kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
minikube service demo-metrics-app --url
```

Whichever way you run it, hit `/health` and `/metrics` on the URL/port
it gives you.

## The pipeline

Three workflows, all trigger on push:

- `pytest.yml` — Dell's original unit tests, now run against Python
  3.10/3.11/3.12, plus a coverage report
- `pylint.yml` — lint check, plus a `pip-audit` job that scans
  `requirements.txt` and only fails on high/critical severity issues
- `demo-pipeline.yml` — installs and tests this app, builds the Docker
  image, scans it with Trivy (same high/critical-only rule)

I commit everything locally and push it myself so I can watch each run
happen in Actions rather than trusting it blind.
