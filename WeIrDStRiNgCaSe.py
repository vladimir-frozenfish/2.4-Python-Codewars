"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
and returns the same string with all even indexed characters in each word upper
cased, and all odd indexed characters in each word lower cased. The indexing
just explained is zero based, so the zero-ith index is even, therefore that
character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words. Words will be
separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'.
"""


def to_weird_case(string):
    string_out = []

    is_low = False
    for i in string:
        if is_low:
            string_out.append(i.lower())
            is_low = False
        elif i == ' ':
            string_out.append(i)
            is_low = False
        else:
            string_out.append(i.upper())
            is_low = True

    return ''.join(string_out)

print(to_weird_case('This'))
print(to_weird_case('is'))
print(to_weird_case('is'))
print(to_weird_case('This is a test'))






'''
test.describe('to_weird_case')

test.it('should return the correct value for a single word')
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')

test.it('should return the correct value for multiple words')
test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')
'''