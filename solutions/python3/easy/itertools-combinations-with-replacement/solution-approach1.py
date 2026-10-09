# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Problem     itertools.combinations_with_replacement()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 11:46 p.m.
# ──────────────────────────────────────────────────

from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)

    # Sort characters lexicographically first
    for combo in combinations_with_replacement(sorted(s), k):
        print(''.join(combo))
