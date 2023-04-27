from prometheus_client import Gauge, Enum
import time
import requests



class AppMetrics:
    """
    AppMetrics is the metrics class in where
    we create our prometheus metrics to collect.
    """
    def __init__(self, app_host="127.0.0.1", app_port=80, metrics_path="", secure=False, polling_interval_seconds=5):        
        self.app_url = f"{'https' if secure else 'http'}://{app_host}:{app_port}/{metrics_path}"
        self.polling_interval_seconds = polling_interval_seconds

        # metrics
        self.current_requests = Gauge("app_requests_current", "Current requests")
        self.pending_requests = Gauge("app_requests_pending", "Pending requests")
        self.total_uptime = Gauge("app_uptime", "Uptime")
        self.health = Enum("app_health", "Health", states=["healthy", "unhealthy"])

    def run(self):
        """
        in run method, we pull the metrics in an interval time.
        """
        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        resp = requests.get(url=self.app_url)
        status_data = resp.json()

        # Update Prometheus metrics with application metrics
        self.current_requests.set(status_data["current_requests"])
        self.pending_requests.set(status_data["pending_requests"])
        self.total_uptime.set(status_data["total_uptime"])
        self.health.state(status_data["health"])
