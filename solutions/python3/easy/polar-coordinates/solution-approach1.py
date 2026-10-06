# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Problem     Polar Coordinates
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 12:51 p.m.
# ──────────────────────────────────────────────────

import cmath

if __name__== '__main__':
    z=complex(input().strip())
    r=abs(z)
    phi=cmath.phase(z)
    
    print(r)
    print(phi)
    

