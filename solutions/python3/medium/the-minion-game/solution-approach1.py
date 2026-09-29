# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 09:38 p.m.
# ──────────────────────────────────────────────────

def minion_game(string):
    vowels = set("AEIOU")
    stuart_score = 0
    kevin_score = 0
    n = len(string)

    for i in range(n):
        points = n - i
        if string[i] in vowels:
            kevin_score += points
        else:
            stuart_score += points

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


    

