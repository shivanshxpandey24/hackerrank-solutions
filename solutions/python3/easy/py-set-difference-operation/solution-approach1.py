# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Problem     Set .difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:57 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    b = int(input())
    french_subs = set(map(int, input().split()))

    # Difference (-) gives students subscribed to English only
    print(len(english_subs - french_subs))
