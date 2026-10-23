# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Problem     Collections.namedtuple()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 11:56 p.m.
# ──────────────────────────────────────────────────-----------------------

from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Student = namedtuple('Student', input().split())

    total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(n))
    print(f"{total_marks / n:.2f}")
