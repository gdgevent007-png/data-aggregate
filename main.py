# main.py
from reader import iter_events
from aggregator import Aggregator
import os
import json

def main():
    agg = Aggregator()
    for ev in iter_events("sample_logs"):
        agg.ingest(ev)
    r = agg.report()
    # format p95 to 2 decimals
    print(f"Count: {r['count']}, Mean: {r['mean']:.2f}, P95: {r['p95']:.2f}")

if __name__ == "__main__":
    main()
