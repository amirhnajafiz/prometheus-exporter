from prometheus_client import start_http_server
import os

from metrics import AppMetrics



def _main():
    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    app_port = int(os.getenv("APP_PORT", "8000"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))

    app_metrics = AppMetrics(
        app_port=app_port,
        polling_interval_seconds=polling_interval_seconds
    )

    start_http_server(exporter_port)
    app_metrics.run()



if __name__ == "__main__":
    _main()