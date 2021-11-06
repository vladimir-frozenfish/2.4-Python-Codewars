"""Complete the solution so that the function will break
up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    s_out = []
    i = 0
    while i < len(s):
        if s[i].isupper():
            s_out.append(' ')
        s_out.append(s[i])
        i += 1
    return ''.join(s_out)


'''
test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
'''

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
print(solution(""))
