# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Problem     Compress the String! 
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-10, 11:50 p.m.
# ──────────────────────────────────────────────────

from itertools import groupby

if __name__ == '__main__':
    s = input().strip()

    # groupby groups consecutive identical characters
    # (len(list(group)), int(key)) formats each consecutive run
    result = [(len(list(group)), int(key)) for key, group in groupby(s)]

    print(*result)
