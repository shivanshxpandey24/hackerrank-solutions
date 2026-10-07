# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true
# Problem     Power - Mod Power
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-07, 02:59 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())

    # Line 1: a raised to the power of b
    print(pow(a, b))

    # Line 2: a raised to the power of b modulo m
    print(pow(a, b, m))
