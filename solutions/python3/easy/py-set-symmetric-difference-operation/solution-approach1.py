# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Problem     Set .symmetric_difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:58 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    b = int(input())
    french_subs = set(map(int, input().split()))

    # Symmetric difference (^) returns elements in either set, but not in both
    print(len(english_subs ^ french_subs))
