# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-11, 11:51 p.m.
# ──────────────────────────────────────────────────-------------------------------

from collections import Counter

if __name__ == '__main__':
    num_shoes = int(input())
    inventory = Counter(map(int, input().split()))
    num_customers = int(input())

    total_earnings = 0

    for _ in range(num_customers):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1

    print(total_earnings)
