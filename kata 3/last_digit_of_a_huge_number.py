"""For a given list [x1, x2, x3, ..., xn] compute
the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g.,

last_digit([3, 4, 2]) == 1
because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast.
For example, 9 ^ (9 ^ 9) has more than 369 millions of digits.
lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1
and that lastDigit of an empty list equals to 1.
"""

def last_digit(lst):
    if lst == []:
        return 1
    elif len(lst) == 1:
        return lst[0] % 10

    lst = [] + lst
    i = len(lst)-1
    while i >= 2:
        if lst[i-1] % 10 == 0 and lst[i-1] != 0:
            lst.pop()
            lst.pop()
            lst.append(100)
        else:
            lst.append(pow(lst.pop(i-1), lst.pop(), 1000))
        i -= 1

    return pow(lst[0], lst[1], 10)

print(last_digit([499942, 898102, 846073]) == 6)




"""
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
"""
