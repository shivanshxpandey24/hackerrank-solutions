# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
# Problem     Iterables and Iterators
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-10, 11:51 p.m.
# ──────────────────────────────────────────────────

from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    letters = input().split()
    k = int(input())

    # Generate all combinations of k elements
    all_combos = list(combinations(letters, k))

    # Count how many combinations contain at least one 'a'
    favorable = sum(1 for combo in all_combos if 'a' in combo)

    # Probability rounded/formatted to 4 decimal places
    print(f"{favorable / len(all_combos):.4f}")
