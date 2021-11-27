"""
You are given a string s. Every letter in s appears once.
Consider all strings formed by rearranging the letters in s.
After ordering these strings in dictionary order,
return the middle term. (If the sequence has a even
length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

The permutations in order are: "abc", "acb",
"bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s
unique letters (2 <= length <= 26)

[output] a string
middle permutation.
"""

def middle_permutation(string):
    point = len(string) // 2

    string = ''.join(sorted(string))

    if len(string) % 2:
        return string[point] + string[point-1] + ''.join(sorted((string[:point-1] + string[point+1:]), reverse=True))
    else:
        return string[point-1] + ''.join(sorted((string[:point-1] + string[point:]), reverse=True))




print(middle_permutation('acijkmnopsv'))
print(middle_permutation('acijkmnopsv') == 'mkvsponjica')


"""
test.assert_equals(middle_permutation("abc"), "bac")
test.assert_equals(middle_permutation("abcd"), "bdca")
test.assert_equals(middle_permutation("abcdx"), "cbxda")
test.assert_equals(middle_permutation("abcdxg"), "cxgdba")
test.assert_equals(middle_permutation("abcdxgz"), "dczxgba")
"""