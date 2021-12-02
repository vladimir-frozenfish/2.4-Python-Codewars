puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

row = set(puzzle[1])

print(row)

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


