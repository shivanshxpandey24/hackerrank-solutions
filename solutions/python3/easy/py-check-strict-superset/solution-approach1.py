 ## ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Problem     Check Strict Superset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 10:06 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    n = int(input())

    is_strict_superset = True

    for _ in range(n):
        other_set = set(map(int, input().split()))
        
        if not (set_a > other_set):
            is_strict_superset = False
            break

    print(is_strict_superset)
