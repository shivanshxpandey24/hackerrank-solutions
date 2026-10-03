# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Problem     Set Mutations
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-03, 08:35 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    _ = int(input())
    set_a = set(map(int, input().split()))
    num_other_sets = int(input())

    for _ in range(num_other_sets):
        operation = input().split()[0]
        other_set = set(map(int, input().split()))
        
        # Execute the in-place set mutation method directly on set_a
        getattr(set_a, operation)(other_set)

    print(sum(set_a))
