# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Problem     Symmetric Difference
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 11:54 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    # Read first set
    m_size = int(input())
    set_m = set(map(int, input().split()))
    
    # Read second set
    n_size = int(input())
    set_n = set(map(int, input().split()))
    
    # Compute symmetric difference using the ^ operator (or set_m.symmetric_difference(set_n))
    sym_diff = set_m ^ set_n
    
    # Sort in ascending order and print each integer on a new line
    for val in sorted(sym_diff):
        print(val)
