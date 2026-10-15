# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
# Problem     Collections.deque()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 11:44 p.m.
# ──────────────────────────────────────────────────

from collections import deque

if __name__ == '__main__':
    n = int(input())
    d = deque()

    for _ in range(n):
        cmd = input().split()
        method = cmd[0]
        if len(cmd) > 1:
            getattr(d, method)(int(cmd[1]))
        else:
            getattr(d, method)()

    print(*d)
