FROM python:3.10-alpine

ENV POLLING_INTERVAL_SECONDS=5
ENV EXPORTER_PORT=9877
ENV TARGET_HOST=node-app
ENV TARGET_PORT=8000
ENV TARGET_METRICS=status

COPY *.py .

EXPOSE $EXPORTER_PORT

CMD python exporter.py