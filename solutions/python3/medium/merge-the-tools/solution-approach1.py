# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 09:56 p.m.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        # dict.fromkeys() removes duplicates while preserving insertion order
        print("".join(dict.fromkeys(substring)))

    
    

