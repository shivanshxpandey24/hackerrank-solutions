# # ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Problem     Check Subset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 10:01 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        _ = int(input())
        set_a = set(map(int, input().split()))
        _ = int(input())
        set_b = set(map(int, input().split()))

        print(set_a.issubset(set_b))
