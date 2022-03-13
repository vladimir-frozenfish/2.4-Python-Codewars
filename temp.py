a = [0, 0]
b = [7, 0]


L = (a[0]-b[0])**2+(a[1]-b[1])**2
L_2 = sum([(a[i]-b[i])**2 for i in range(2)])

L_1 = 0
for i in range(2):
    L_1 += (a[i]-b[i])**2

x = lambda a:__import__('math').sqrt(a) + __import__('math').sqrt(a)

print(x(25))

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


