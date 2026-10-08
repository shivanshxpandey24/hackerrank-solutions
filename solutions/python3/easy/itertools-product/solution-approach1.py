# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-08, 06:19 p.m.
# ──────────────────────────────────────────────────

from itertools import product

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Compute cartesian product and unpack with spaces
    print(*product(a, b))
