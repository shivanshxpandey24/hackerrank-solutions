# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true
# Problem     Triangle Quest
# Difficulty  Medium
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-08, 06:04 p.m.
# ──────────────────────────────────────────────────

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i // 9) * i)
