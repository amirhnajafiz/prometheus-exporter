# Prometheus Exporter

Implementing a Prometheus exporter with Python. Prometheus follows an ```HTTP pull model```,
It scrapes Prometheus ```metrics``` from endpoints routinely. Typically the abstraction layer between the application and Prometheus is an exporter,
which takes application-formatted ```metrics``` and converts them to Prometheus ```metrics``` for consumption.

## Why exporter?

You might need to write your own exporter if:

- You are using 3rd party software that does not have an existing exporter already
- You want to generate Prometheus ```metrics``` from software that you have written

## Example



### Response

Exporter provides the following output, which are prometheus ```metrics```.

```shell
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 626.0
python_gc_objects_collected_total{generation="1"} 33.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 54.0
python_gc_collections_total{generation="1"} 4.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="10",patchlevel="0",version="3.10.0"} 1.0
# HELP app_requests_current Current requests
# TYPE app_requests_current gauge
app_requests_current 4.0
# HELP app_requests_pending Pending requests
# TYPE app_requests_pending gauge
app_requests_pending 0.0
# HELP app_uptime Uptime
# TYPE app_uptime gauge
app_uptime 104.914734
# HELP app_health Health
# TYPE app_health gauge
app_health{app_health="healthy"} 1.0
app_health{app_health="unhealthy"} 0.0
```

## Resources

- [https://trstringer.com](https://trstringer.com/quick-and-easy-prometheus-exporter/)
