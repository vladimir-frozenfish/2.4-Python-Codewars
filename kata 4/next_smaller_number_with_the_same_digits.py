"""
Write a function that takes a positive integer and returns
the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None),
when there is no smaller number that contains the same digits.
Also return -1 when the next smaller number with the same
digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
"""


def next_smaller(n):
    number = [int(a) for a in str(n)]
    dlinna = len(number)

    for i in range(dlinna - 2, -1, -1):
        for j in range(i + 1, dlinna):
            number = number[:i + 1] + sorted(number[i + 1:], reverse=True)
            if number[i] > number[j] and (i != 0 or number[j] != 0):
                number[i], number[j] = number[j], number[i]
                return (int(''.join(map(str, number))))

    return -1




print(next_smaller(1422135) == 1421532)
print(next_smaller(907) == 790)
print(next_smaller(100) == -1)
print(next_smaller(531) == 513)
print(next_smaller(123456798) == 123456789)
print(next_smaller(135) == -1)
print(next_smaller(2071) == 2017)
print(next_smaller(414) == 144)
print(next_smaller(123456789) == -1)
print(next_smaller(1234567908) == 1234567890)
print(next_smaller(1234567908))
print(next_smaller(908) == 890)
print(next_smaller(190) == 109)


"""
test.it("Smaller numbers")
test.assert_equals(next_smaller(907), 790)
test.assert_equals(next_smaller(531), 513)
test.assert_equals(next_smaller(135), -1)
test.assert_equals(next_smaller(2071), 2017)
test.assert_equals(next_smaller(414), 144)
test.assert_equals(next_smaller(123456798), 123456789)
test.assert_equals(next_smaller(123456789), -1)
test.assert_equals(next_smaller(1234567908), 1234567890)
"""



"""
# if number[i] > number[j]:
# if number[i] > number[j] and i != 0 or (i == 0 and number[j] != 0 and number[i] > number[j]):
# if number[i] > number[j] and (i != 0 or (i == 0 and number[j] != 0)):
"""