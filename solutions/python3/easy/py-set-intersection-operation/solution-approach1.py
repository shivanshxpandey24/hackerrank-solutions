# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Problem     Set .intersection() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 11:52 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    english_subs = set(map(int, input().split()))
    b = int(input())
    french_subs = set(map(int, input().split()))

    # Intersection (&) gives the students subscribed to both newspapers
    print(len(english_subs & french_subs))
