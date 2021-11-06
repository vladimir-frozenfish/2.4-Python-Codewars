"""
Write a function that takes a string of parentheses,
and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis,
input may contain any valid ASCII characters. Furthermore,
the input string may be empty and/or not contain any
parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
    count = 0
    for i in string:
        if i not in '()':
            continue
        elif i == ')':
            if count == 0:
                return False
            else:
                count -= 1
        else:  # если i == '('
            count += 1
    return count == 0


print(valid_parentheses("  (") == False)
print(valid_parentheses(")test") == False)
print(valid_parentheses("") == True)
print(valid_parentheses("hi())(") == False)
print(valid_parentheses("hi(hi)()") == True)


'''
    test.assert_equals(valid_parentheses("  ("), False)
    test.assert_equals(valid_parentheses(")test"), False)
    test.assert_equals(valid_parentheses(""), True)
    test.assert_equals(valid_parentheses("hi())("), False)
    test.assert_equals(valid_parentheses("hi(hi)()"), True)
'''