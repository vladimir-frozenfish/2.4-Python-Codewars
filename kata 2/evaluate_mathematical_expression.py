"""
Instructions
Given a mathematical expression as a string you must
return the result as a number.

Numbers
Number may be both whole numbers and/or decimal numbers.
The same goes for the returned result.

Operators
You need to support the following mathematical operators:

Multiplication *
Division / (as floating point division)
Addition +
Subtraction -
Operators are always evaluated from left-to-right,
and * and / must be evaluated before + and -.

Parentheses
You need to support multiple levels of nested
parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace
There may or may not be whitespace
between numbers and operators.

An addition to this rule is that the minus sign (-) used
for negating numbers and parentheses will never be separated
by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10
And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid
Validation
You do not need to worry about validation -
you will only receive valid mathematical expressions
following the above rules.

Restricted APIs
NOTE: eval and exec are disallowed in your solution.
"""


def amount(expression):
    """функция посчета суммы двух чисел"""
    return expression[0] + expression[2]

def difference(expression):
    """функция посчета разности двух чисел"""
    return expression[0] - expression[2]

def multiplication(expression):
    """функция посчета произведение двух чисел"""
    return expression[0] * expression[2]

def division(expression):
    """функция посчета частного двух чисел"""
    return expression[0] / expression[2]

def from_string_to_list(math_string):
    """функция перевода математического выражения
    из строки в список"""
    math_string = math_string.replace(' ', '')
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    math_list = []
    number = ''

    for i in range(len(math_string)):
        if math_string[i] in numbers:
            number += math_string[i]
            if math_string[i+1:i+2] not in numbers:
                math_list.append(int(number))
                number = ''
        elif math_string[i] == '-' and math_string[i-1:i] not in numbers:
            math_list.append(-1)
            math_list.append('*')
        else:
            math_list.append(math_string[i])

    return math_list

def calc(expression):
    math_def = {
        '+': amount,
        '-': difference,
        '*': multiplication,
        '/': division
    }

    """вызов функции перевода математического 
    выражения из строки в список"""
    math_list = (from_string_to_list(expression))

    """список для помещения туда двух чисел и действия"""
    math_expression = []


    while len(math_list) > 1:
        """помещение в выражение сначала действий где есть * или /"""
        i = 1
        while '*' in math_list or '/' in math_list:
            if math_list[i] == '*' or math_list[i] == '/':
                math_expression.append(math_list[i - 1])
                math_expression.append(math_list[i])
                math_expression.append(math_list[i + 1])

                del math_list[i-1:i + 2]
                math_list.insert(i-1, math_def[math_expression[1]](math_expression))
                math_expression = []

                i = 1
            else:
                i += 1

        """помещение в выражение двух чисел и действие
        пока последовательно для простого выражения без скобок"""
        i = 0
        math_expression.append(math_list[i])
        math_expression.append(math_list[i+1])
        math_expression.append(math_list[i+2])

        del math_list[i:i+3]
        math_list.insert(i, math_def[math_expression[1]](math_expression))
        math_expression = []

    return math_list[0]


print(calc('2+2-6/6+18*2/3+-1'))


"""
("1 + 1", 2),
("8/16", 0.5),
("3 -(-1)", 4),
("2 + -2", 0),
("10- 2- -5", 13),
("(((10)))", 10),
("3 * 5", 15),
("-7 * -(6 / 3)", 14)
"""