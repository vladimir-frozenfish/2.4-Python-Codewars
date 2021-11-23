x = [1, 2, 5, 4]
if x[2]:
    print(True)
else:
    print(False)

add_j = {0: (0, 1, 2),
         3: (3, 4, 5),
         6: (6, 7, 8)}

add_i = {0: 0,
         1: 0,
         2: 0,
         3: 3,
         4: 3,
         5: 4,
         6: 6,
         7: 6,
         8: 6,
         }

abc = [[123],
       [456],
       [789]]

df = [[123],
       [13],
       [789]]


if [200] not in abc and [200] not in df:
    print('yes')
else:
    print('no')


'''
matrix = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]

matrix = list(zip(*matrix))[::-1]  # Rotate
print(matrix)
'''


"""down"""
"""
matrix = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]

snail_path = [1]

if type(matrix[0]) != list:
    snail_path += matrix.pop()
else:
    for i in range(0, len(matrix)):
        snail_path.append(matrix[i].pop())

print(snail_path)
print(matrix)
"""


