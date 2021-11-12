x = [1, 2, 3, 4]
x.insert(10, 5)
print(x)
del x[1:3]
print(x)



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


