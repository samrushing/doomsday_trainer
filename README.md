# doomsday_trainer

This is a utility to help quiz yourself on day-of-the-week calculations, using John Conway's "Doomsday" system.

 https://en.wikipedia.org/wiki/Doomsday_rule

We use the "odd + 11" technique for calculating year anchors.

A quick description of the technique, which can be done in your head with some practice:

The idea is that there's a set of dates that ALWAYS fall on the same
day within a given year.  This set of dates is pretty easy to
remember.  See the wikipedia tables for more info, but the
following can get you started:

Anchor day for the century:

 * You will need to memorize only a little information.
 *  Every century there's an 'anchor day'.
 *  For 19xx it's Wed, for 20xx it's Tue.
 *  [in python: [2, 0, 5, 3][C % 4]]

Anchor day for the year:

 *  T = last two digits of the year
 *  if T is odd, add 11
 *  T = T/2
 *  if T is odd, add 11
 *  T = T % 7
 *  T = 7 - T

 eg. 1999.

   T = 99, 110, 55, 66, 3, 4.

so the offset for 1999 is FOUR.  Add it to the century anchor, Wed, to get Sun.

NOW, all the Doomsdays of 1999 will fall on Sunday.

Doomsdays for any year:

 1:(3|4)  2:28|29  3:14  4:4  5:9  6:6  7:11  8:8  9:5  10:10 11:7 12:12

For example, March 14th (Pi Day!) is a Doomsday.  So is June 6th.
  9-to-5 and 5-to-9.  (Sep 5 and May 9).  7-11 and 11-7.
  4/6/8/10/12 are all x:x pattern, aug 8, dec 12, etc.

Only Jan/Feb are tricky, because of leap years.
  If it's a leap year, then Jan 4, otherwise Jan 3.
  If it's a leap year, then Feb 29, otherwise Feb 28.
