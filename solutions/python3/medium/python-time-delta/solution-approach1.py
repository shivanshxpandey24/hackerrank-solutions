# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
# Problem     Time Delta
# Difficulty  Medium
# Subdomain   Date and Time
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-16, 03:01 p.m.
# ──────────────────────────────────────────────────

from datetime import datetime

# Format string matching: "Day dd Mon yyyy hh:mm:ss +xxxx"
# e.g., "Sun 10 May 2015 13:54:36 -0700"
FMT = "%a %d %b %Y %H:%M:%S %z"

def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, FMT)
    dt2 = datetime.strptime(t2, FMT)
    return str(int(abs((dt1 - dt2).total_seconds())))

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        print(time_delta(t1, t2))
