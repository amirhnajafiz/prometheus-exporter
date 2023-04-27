from prometheus_client import start_http_server
import os

from metrics import AppMetrics



def _main():
    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))

    app_metrics = AppMetrics(
        app_host="localhost",
        app_port="8000",
        secure=False,
        metrics_path="status",
        polling_interval_seconds=polling_interval_seconds
    )

    start_http_server(exporter_port)
    print(f'exporter start on :{exporter_port} ...')
    
    app_metrics.run()



if __name__ == "__main__":
    _main()