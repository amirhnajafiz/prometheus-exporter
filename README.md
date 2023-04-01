# Prometheus Exporter

Implementing a Prometheus exporter with Python. Prometheus follows an ```HTTP pull model```,
It scrapes Prometheus ```metrics``` from endpoints routinely. Typically the abstraction layer between the application and Prometheus is an exporter,
which takes application-formatted ```metrics``` and converts them to Prometheus ```metrics``` for consumption.

## Why exporter?

You might need to write your own exporter if:

- You are using 3rd party software that does not have an existing exporter already
- You want to generate Prometheus ```metrics``` from software that you have written

## Resources

- [https://trstringer.com](https://trstringer.com/quick-and-easy-prometheus-exporter/)
