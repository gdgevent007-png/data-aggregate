# aggregator.py
import math

def percentile(sorted_values, p):
    """
    p in [0,1]. Use simple linear interpolation between neighbours.
    """
    if not sorted_values:
        return None
    n = len(sorted_values)
    # use (n-1)*p index for interpolation
    k = (n - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(sorted_values[int(k)])
    d0 = sorted_values[f] * (c - k)
    d1 = sorted_values[c] * (k - f)
    return float(d0 + d1)

class Aggregator:
    def __init__(self):
        self.values = []

    def ingest(self, ev):
        # ensure numbers and coerce to float
        try:
            v = float(ev.get("value", 0))
        except Exception:
            v = 0.0
        self.values.append(v)

    def report(self):
        if not self.values:
            return {}
        v = sorted(self.values)
        mean = sum(v) / len(v)
        p95 = percentile(v, 0.95)
        return {"count": len(v), "mean": mean, "p95": p95}
