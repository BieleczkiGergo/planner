This is a program made for time arrangement. It can keep track of time schedules (not just one),
and can compare schedules.

The rangeList:
Basically, a list of ranges, from numbers. It only has a list of numbers as for it's data.
Everything else is only functions. It can be represented as a clock signal, where the numbers
represent the changes in the clock. Therefore, it's a binary type, so it can only be operated
using logical operators. This makes it the optimal data structure for time arrangement, as you
can just "and" two of these together and see when both of them are empty.

It also has an event system, which basically just keeps track of the "up" cycles of the rangeList
and names them. It also keeps track of multiple people.