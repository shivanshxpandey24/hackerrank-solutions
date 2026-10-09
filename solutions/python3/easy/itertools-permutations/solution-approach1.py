# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 11:43 p.m.
# ──────────────────────────────────────────────────

from itertools import permutations

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)

    # Sort the string first so permutations are generated in lexicographic order
    for p in permutations(sorted(s), k):
        print(''.join(p))
