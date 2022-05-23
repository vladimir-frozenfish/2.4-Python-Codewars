"""
Write a function called sumIntervals/sum_intervals()
that accepts an array of intervals, and returns the sum
 of all the interval lengths.
 Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:
[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4]
and [3, 5] overlap, we can treat the interval as [1, 5],
which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
"""


def counting_sum_of_intervals(result_list):
    sum_interval = 0

    for s in range(0, len(result_list), 2):
        sum_interval += result_list[s+1] - result_list[s]

    return sum_interval

'''
def sum_of_intervals(intervals):
    result_list = [0, 0]

    """цикл по всем интервалам"""
    for pair in intervals:
        print('Промежуток:', result_list)
        left_barier = 0
        right_barier = 0

        left_valeu = pair[0]
        right_value = pair[1]

        """цикл по результирующему списку интервалов.
        за раз берется один интервал (два числа)
        чикл с конца
        проверка для левого значени интервала"""
        for i in range(len(result_list)-1, -1, -2):

            """первая проверка - если первое значение интервала меньше первого 
            значение в результирующем списке, то оно сразу добавляется в список 
            вначале дважы, для сохранения парности интервалов"""
            if left_valeu < result_list[0]:
                result_list.insert(0, left_valeu)
                result_list.insert(0, left_valeu)
                break

            """если проверяемое значение больше последнего
            значения, то
            он добавляется в результирующий лист дважды, для сохранения
            парности интервалов"""
            if left_valeu > result_list[i]:
                result_list.insert(i+1, left_valeu)
                result_list.insert(i+1, left_valeu)
                left_barier = i+1
                break
            elif left_valeu <= result_list[i] and left_valeu >= result_list[i-1]:
                left_barier = i-1
                break

        """цикл по результирующему списку интервалов.
        за раз берется один интервал (два числа)
        цикл с конца проверка для правого значени интервала"""
        for i in range(len(result_list) - 1, -1, -2):

            """если проверяемое значение больше последнего
            значения, то он добавляется в результирующий лист"""
            if right_value > result_list[i]:
                result_list.insert(i + 1, right_value)
                right_barier = i + 1
                break
            elif right_value <= result_list[i] and right_value >= result_list[i - 1]:
                right_barier = i
                break

        """удаление лишних интервалов в границах барьеров"""
        del result_list[left_barier+1 : right_barier]

    print('Финиш:', result_list)

    return counting_sum_of_intervals(result_list)
'''

def sum_of_intervals(intervals):
    result_list = [0, 0]

    """цикл по всем интервалам"""
    for pair in intervals:
        print('Промежуток:', result_list)
        left_barier = 0
        right_barier = 0

        left_valeu = pair[0]
        right_value = pair[1]

        """цикл по результирующему списку интервалов.
        за раз берется один интервал (два числа)
        чикл с конца
        проверка для левого значени интервала"""
        if left_valeu < result_list[0]:
            result_list.insert(0, left_valeu)
            result_list.insert(0, left_valeu)
        else:
            for i in range(len(result_list)-1, -1, -2):
                """если проверяемое значение больше последнего
                значения, то
                он добавляется в результирующий лист дважды, для сохранения
                парности интервалов"""
                if left_valeu > result_list[i]:
                    result_list.insert(i+1, left_valeu)
                    result_list.insert(i+1, left_valeu)
                    left_barier = i+1
                    break
                elif left_valeu <= result_list[i] and left_valeu >= result_list[i-1]:
                    left_barier = i-1
                    break

        """цикл по результирующему списку интервалов.
        за раз берется один интервал (два числа)
        цикл с конца проверка для правого значени интервала"""
        for i in range(len(result_list) - 1, -1, -2):

            """если проверяемое значение больше последнего
            значения, то он добавляется в результирующий лист"""
            if right_value > result_list[i]:
                result_list.insert(i + 1, right_value)
                right_barier = i + 1
                break
            elif right_value <= result_list[i] and right_value >= result_list[i - 1]:
                right_barier = i
                break

        """удаление лишних интервалов в границах барьеров"""
        del result_list[left_barier+1 : right_barier]

    print('Финиш:', result_list)

    return counting_sum_of_intervals(result_list)


# интервалы без вхождений друг в друга и последующий больше предыдующего
print(sum_of_intervals([(1, 4), (6, 10), (12, 16)]) == 11)



print(sum_of_intervals([(1, 5)]) == 4)
#print(sum_of_intervals([(1, 5), (6, 10)]) == 8)
#print(sum_of_intervals([(1, 5), (1, 5)]) == 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)

#print(sum_of_intervals([(1, 4), (7, 10), (3, 5), (0, 20)]) == 20)

print(sum_of_intervals([[1,5],[10, 20],[1, 6],[16, 19],[5, 11], [-5, -3]]) == 21)



'''
test.assert_equals(sum_of_intervals([(1, 5)]), 4)
test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
'''