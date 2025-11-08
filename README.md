# data-aggregate-plus

**Goal:** Read newline JSON lines from `sample_logs/` and compute:
- Count of records
- Mean of the `value` field
- 95th percentile (P95) with linear interpolation

**Run**
```bash
python main.py

```

Slight hint:

Percentile calculation must use interpolation (use (n-1)*p method). Also be careful with trailing whitespace in log lines.

Deliverable:

Program prints Count: 4, Mean: 41.25, P95: 50.00.
