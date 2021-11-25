"""возвращает последнюю цифру числа после n1 ** n2"""

def last_digit(n1, n2):
    first_number = n1 % 10

    simple_list = [0, 1, 5, 6]
    if n2 == 0:
        return 1
    elif first_number in simple_list:
        return first_number


    second_number = n2 % 4
    result_dict = {
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6, 4, 6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1, 9, 1]
    }

    return result_dict[first_number][second_number-1]



print(last_digit(9, 7) == 9)
print(last_digit(10, 10 ** 10) == 0)
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) == 7)
print(last_digit(2 ** 200, 2 ** 300) == 6)
"""
test.it("Example tests")
test.assert_equals(last_digit(4, 1), 4)
test.assert_equals(last_digit(4, 2), 6)
test.assert_equals(last_digit(9, 7), 9)
test.assert_equals(last_digit(10, 10 ** 10), 0)
test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)
"""