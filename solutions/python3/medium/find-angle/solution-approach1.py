# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Problem     Find Angle MBC
# Difficulty  Medium
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 01:43 p.m.
# ──────────────────────────────────────────────────

import cmath
import math

if __name__ == '__main__':
    ab = float(input())
    bc = float(input())

    # Hypotenuse AC using Pythagoras theorem
    ac = (ab**2 + bc**2) ** 0.5

    # Ratio sin(theta) = AB / AC
    sin_val = ab / ac

    # cmath.asin() returns a complex number, take .real for the angle in radians
    angle_rad = cmath.asin(sin_val).real

    # Convert to degrees
    angle_deg = math.degrees(angle_rad)

    # Round to nearest integer (round-half-up rule)
    res = int(math.floor(angle_deg + 0.5))

    # Output with the degree symbol
    print(f"{res}\u00b0")
