"""
Snail Sort
Given an n x n array, return the array elements arranged
from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest
value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

def right(snail_map: list, snake_path: list):
    """чтение верхней строки справа-налева
    добавлениее её в snake_path и
    удаление из snail_map"""
    snake_path += snail_map.pop(0)
    return snail_map, snake_path, 'down'

def down(snail_map: list, snake_path: list):
    """чтение последнего столбика от верха-к низу
    добавлениее его в snake_path и
    удаление из snail_map"""
    if type(snail_map[0]) != list:
        snake_path.append(matrix.pop())
    else:
        for i in range(0, len(snail_map)):
            snake_path.append(snail_map[i].pop())

    return snail_map, snake_path, 'left'

def left(snail_map: list, snake_path: list):
    """чтение нижней строки в обратном порядке
    добавлениее её в snake_path и
    удаление из snail_map"""
    temp = snail_map.pop()
    temp.reverse()
    snake_path += temp

    return snail_map, snake_path, 'up'

def up(snail_map: list, snake_path: list):
    """чтение првого столбика от низа-к верху
    добавлениее его в snake_path и
    удаление из snail_map"""
    if type(snail_map[0]) != list:
        snake_path.append(matrix.pop(0))
    else:
        for i in range(len(snail_map)-1, -1, -1):
            snake_path.append(snail_map[i].pop(0))

    return snail_map, snake_path, 'right'

def snail(snail_map):
    snail_map = snail_map
    snake_path = []

    vector = 'right'
    vector_def = {'right': right,
                  'down': down,
                  'left': left,
                  'up': up}

    while snail_map != []:

        snail_map, snake_path, vector = vector_def[vector](snail_map, snake_path)
        #print(snail_map, snake_path, vector)


    return snake_path

# тест 1
matrix = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]

snail_path = snail(matrix)

print(snail_path)
print(snail_path == [1, 2, 3, 4, 5, 6, 7, 8, 9])

# тест 2
matrix = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24]]

snail_path = snail(matrix)

print(snail_path)
print(snail_path == [1, 2, 3, 4, 5, 6, 12, 18, 24, 23, 22, 21, 20, 19, 13, 7, 8, 9, 10, 11, 17, 16, 15, 14])


'''
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)
'''