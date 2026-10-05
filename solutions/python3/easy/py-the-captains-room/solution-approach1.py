# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Problem     The Captain's Room 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 11:54 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))

    # Mathematical formulation:
    # (k * sum(unique_rooms) - sum(all_rooms)) // (k - 1)
    unique_rooms = set(rooms)
    captains_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

    print(captains_room)
