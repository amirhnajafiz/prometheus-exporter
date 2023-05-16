from prometheus_client import start_http_server
import os

from metrics import AppMetrics



def _main():
    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))
    
    host = os.getenv("TARGET_HOST", "localhost")
    port = int(os.getenv("TARGET_PORT", "8000"))
    path = os.getenv("TARGET_METRICS", "status")

    app_metrics = AppMetrics(
        app_host=host,
        app_port=port,
        secure=False,
        metrics_path=path,
        polling_interval_seconds=polling_interval_seconds
    )

    start_http_server(exporter_port)
    print(f'exporter start on :{exporter_port} ...')
    
    app_metrics.run()



if __name__ == "__main__":
    _main()
