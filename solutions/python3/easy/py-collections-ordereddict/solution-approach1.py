# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Problem     Collections.OrderedDict()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 11:57 p.m.
# ──────────────────────────────────────────────────

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    items = OrderedDict()

    for _ in range(n):
        # rsplit from the right by 1 space to separate name and price
        item_name, net_price = input().rsplit(' ', 1)
        net_price = int(net_price)
        
        # Accumulate net price while maintaining first-occurrence order
        items[item_name] = items.get(item_name, 0) + net_price

    for item, price in items.items():
        print(f"{item} {price}")
