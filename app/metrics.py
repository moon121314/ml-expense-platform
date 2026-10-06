"""Prometrics metrics."""
from prometheus_client import Counter,Histogram

PREDICTION_COUNTER = Counter(
    "predictions_total",
    "Total number of predictions",
    ["category"],
)

PREDICTION_LATENCY = Histogram("prediction_latency_seconds","Time spend processing requests")