'''
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that, when added together, give the target value.
The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/
'''

def two_sum(numbers, target):
    two_sum_index = ()

    for i in range(len(numbers)-1):
        a = numbers[i]
        b = target - a
        if b in numbers[i+1 :]:
            two_sum_index = (i, i + 1 + numbers[i+1 : ].index(b))
            return two_sum_index
            break

print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([1, 0, 0, 0, 1], 2))
print(two_sum([0, 0], 0))

'''
test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])
'''