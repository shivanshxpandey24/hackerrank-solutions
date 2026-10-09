# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Problem     itertools.combinations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 11:44 p.m.
# ──────────────────────────────────────────────────

from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)

    # Sort characters lexicographically first
    sorted_s = sorted(s)

    # Generate combinations for each size from 1 up to k
    for r in range(1, k + 1):
        for combo in combinations(sorted_s, r):
            print(''.join(combo))
