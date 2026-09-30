# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 10:10 p.m.
# ──────────────────────────────────────────────────

def average(array):
    # Convert array to a set to remove duplicate values
    distinct_elements = set(array)
    
    # Calculate sum divided by count of distinct elements
    return sum(distinct_elements) / len(distinct_elements)

