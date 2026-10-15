######## ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Problem     Word Order
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 11:59 p.m.
# ──────────────────────────────────────────────────

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    word_counts = OrderedDict()

    for _ in range(n):
        word = input().strip()
        word_counts[word] = word_counts.get(word, 0) + 1

    # Number of distinct words
    print(len(word_counts))

    # Occurrences of each distinct word in order of appearance
    print(*word_counts.values())
