#### ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Problem     DefaultDict Tutorial
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 12:00 a.m.
# ──────────────────────────────────────────────────---------------------

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())

    # Map each word to a list of its 1-based indices in group A
    group_a = defaultdict(list)
    for i in range(1, n + 1):
        word = input().strip()
        group_a[word].append(str(i))

    # For each word in group B, print indices or -1 if not found
    for _ in range(m):
        word = input().strip()
        if word in group_a:
            print(" ".join(group_a[word]))
        else:
            print("-1")
