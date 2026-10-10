# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Problem     Maximize It!
# Difficulty  Hard
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-10, 11:53 p.m.
# ──────────────────────────────────────────────────

from itertools import product

if __name__ == '__main__':
    k, m = map(int, input().split())

    # Read each line, skipping the first integer (Ni)
    lists = [list(map(int, input().split()))[1:] for _ in range(k)]

    # Compute cartesian product across all K lists and find max sum(x**2) % m
    max_s = max(sum(x**2 for x in combo) % m for combo in product(*lists))

    print(max_s)
