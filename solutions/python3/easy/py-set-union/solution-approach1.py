# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Problem     Set .union() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:51 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    b = int(input())
    french_subs = set(map(int, input().split()))

    # Union operation gives students subscribed to at least one newspaper
    print(len(english_subs | french_subs))
