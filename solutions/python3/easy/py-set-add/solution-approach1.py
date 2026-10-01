# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Problem     Set .add() 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-01, 11:41 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    stamps = set()

    for _ in range(n):
        stamps.add(input().strip())

    print(len(stamps))
