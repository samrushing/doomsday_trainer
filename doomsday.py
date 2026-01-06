# -*- Python -*-

# This is a utility to help quiz yourself on day-of-the-week
#   calculations, using John Conway's "Doomsday" system.
#
# https://en.wikipedia.org/wiki/Doomsday_rule
#
# We use the "odd + 11" technique for calculating year anchors.
#
# A quick description of the technique, which can be done in your head
#   with some practice:
#
# The idea is that there's a set of dates that ALWAYS fall on the same
#   day within a given year.  This set of dates is pretty easy to
#   remember.  See the wikipedia tables for more info, but the
#   following can get you started:
#
# Anchor day for the century:
#
#   You will need to memorize only a little information.
#   Every century there's an 'anchor day'.
#   For 19xx it's Wed, for 20xx it's Tue.
#   [in python: [2, 0, 5, 3][C % 4]]
#
# Anchor day for the year:
#
#   T = last two digits of the year
#   if T is odd, add 11
#   T = T/2
#   if T is odd, add 11
#   T = T % 7
#   T = 7 - T
#
# eg. 1999.
#   T = 99, 110, 55, 66, 3, 4.
# so the offset for 1999 is FOUR.  Add it to the century anchor, Wed, to get Sun.
#
# NOW, all the Doomsdays of 1999 will fall on Sunday.
#
# Doomsdays for any year:
#
# 1:(3|4)  2:28|29  3:14  4:4  5:9  6:6  7:11  8:8  9:5  10:10 11:7 12:12
#
# For example, March 14th (Pi Day!) is a Doomsday.  So is June 6th.
#   9-to-5 and 5-to-9.  (Sep 5 and May 9).  7-11 and 11-7.
#   4/6/8/10/12 are all x:x pattern, aug 8, dec 12, etc.
#
# Only Jan/Feb are tricky, because of leap years.
#   If it's a leap year, then Jan 4, otherwise Jan 3.
#   If it's a leap year, then Feb 29, otherwise Feb 28.
#

import datetime
import calendar
import time

def DOW (n):
    return calendar.day_name[n-1]

def MOY (n):
    return calendar.month_name[n]

# note: gregorian only starts oct 15 1582.

def century_anchor (C):
    # 1600 = 2
    # pattern repeats as 2, 0, 5, 3, ...
    # or just memorize: 19xx = wednesday 20xx = tuesday
    return [2, 0, 5, 3][C % 4]

def odd (n):
    return n % 2 == 1

# odd + 11 method
def year_anchor (n):
    c, T = divmod (n, 100)
    ca = century_anchor (c)
    if odd(T):
        T += 11
    T = T // 2
    if odd(T):
        T += 11
    offset = 7 - (T % 7)
    return (ca + offset) % 7

def handhold_anchor (n):
    c, T = divmod (n, 100)
    ca = century_anchor (c)
    print (f'century anchor = {ca} ({DOW(ca)})')
    print (f'T = {T} which is {["EVEN", "ODD"][T % 2]}')
    if odd(T):
        T += 11
        print (f'PLUS 11 = {T}')
    T //= 2
    print (f'DIVIDE BY 2 = {T}')
    print (f'  which is {["EVEN", "ODD"][T % 2]}')
    if odd (T):
        T += 11
        print (f'PLUS 11 = {T}')
    print (f'    T = {T}')
    T = T % 7
    print (f'T % 7 = {T}')
    off = 7 - T
    print (f'7 - T = {off}')
    r = (ca + off) % 7
    print (f'century {DOW(ca)} + offset {off} = {r} ({DOW(r)})')

def anchor_quiz():
    import random
    print (f'hints: 16xx=tue   17xx=sun   18xx=fri   19xx=wed   20xx=tue')
    while 1:
        y = random.randint (1700, 2100)
        line = input (f'year {y} anchor? ')
        if not line:
            break
        else:
            a0 = int (line)
            a1 = year_anchor (y)
            if a0 != a1:
                print (f'Wrong!')
                handhold_anchor (y)
            else:
                print (f'*** Yes! ***')

dow_hint = "1:(3|4)  2:28|29  3:14  4:4  5:9  6:6  7:11  8:8  9:5  10:10 11:7 12:12"

def handhold_dow (y, m, d):
    import calendar
    ya = year_anchor (y)
    print (dow_hint)
    tc = calendar.TextCalendar (6)
    tc.prmonth (y, m)


def quiz1 (d):
    #print (f'{d.ctime()}')
    now = int (time.time())
    y = d.year
    m = d.month
    day = d.day
    wday = d.isoweekday() % 7
    mname = MOY (m)
    print (f'{y} {mname} {day}')
    line = input ('day [0-6]? ')
    if not line:
        return True
    else:
        day0 = int (line)
        if day0 == wday:
            print (f'*** YES! *** ({int (time.time() - now)}s)')
        else:
            print (f"NOPE.  it's {wday} ({DOW(wday)})")
            handhold_anchor (y)
            handhold_dow (y, m, d)
        return False

def quiz():
    # isoweekday return 1..7 mon=1, so just %7 it.
    # 1900/1/1 .. 2100/1/1
    import random
    while 1:
        jday = random.randint (693596, 766645)
        print (f'ordinal: {jday}')
        d = datetime.date.fromordinal (jday)
        if quiz1 (d):
            break
        else:
            print ('------------')


if __name__ == '__main__':
    import sys
    if '-a' in sys.argv:
        anchor_quiz()
    elif len(sys.argv) == 4:
        # doomsday 1999 5 21
        y, m, d = [int(x) for x in sys.argv[1:]]
        dtd = datetime.date (y, m, d)
        quiz1 (dtd)
    else:
        quiz()
