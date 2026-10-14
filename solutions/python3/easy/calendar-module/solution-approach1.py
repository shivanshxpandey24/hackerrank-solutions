# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# Problem     Calendar Module
# Difficulty  Easy
# Subdomain   Date and Time
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 11:45 p.m.
# ──────────────────────────────────────────────────

import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    
    # calendar.weekday returns 0 for Monday, 1 for Tuesday, ... 6 for Sunday
    day_idx = calendar.weekday(year, month, day)
    
    # calendar.day_name holds full day names in uppercase/lowercase
    print(calendar.day_name[day_idx].upper())
