"""Simple tests for the demo metrics Flask app.

These only exercise the app's own routes and the mocked PowerStore
connection defined in app.py - no real array, no network calls.
"""

from demo_metrics_app.app import app


def get_client():
    """Return a Flask test client for the app."""
    app.testing = True
    return app.test_client()


def test_health_returns_ok():
    """/health should report 200 and a simple ok status."""
    response = get_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_metrics_returns_prometheus_text_format():
    """/metrics should respond with the Prometheus text content type."""
    response = get_client().get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.content_type


def test_metrics_includes_mocked_powerstore_gauges():
    """/metrics should include the mocked PowerStore gauges."""
    body = get_client().get("/metrics").get_data(as_text=True)
    assert "powerstore_appliance_cpu_usage_percent" in body
    assert "powerstore_appliance_memory_usage_percent" in body
    assert "powerstore_appliance_disk_usage_percent" in body
