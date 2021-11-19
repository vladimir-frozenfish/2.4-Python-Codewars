"""
Create a function that takes a positive integer
and returns the next bigger number that can be
formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071

If the digits can't be rearranged to form
a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
"""

def next_bigger(n):
    number = [int(a) for a in str(n)]
    dlinna = len(number)

    for i in range(dlinna - 2, -1, -1):
        for j in range(i + 1, dlinna):
            number = number[:i + 1] + sorted(number[i + 1:])
            if number[i] < number[j] and (i != 0 or number[j] != 0):
                number[i], number[j] = number[j], number[i]
                return (int(''.join(map(str, number))))

    return -1


print(next_bigger(12) == 21)
print(next_bigger(513) == 531)
print(next_bigger(2017) == 2071)
print(next_bigger(414) == 441)
print(next_bigger(144) == 414)
print(next_bigger(9) == -1)
print(next_bigger(111) == -1)
print(next_bigger(531) == -1)



'''
test.assert_equals(next_bigger(12), 21)
test.assert_equals(next_bigger(513), 531)
test.assert_equals(next_bigger(2017), 2071)
test.assert_equals(next_bigger(414), 441)
test.assert_equals(next_bigger(144), 414)
'''