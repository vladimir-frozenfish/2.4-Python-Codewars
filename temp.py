A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]
b = 7

print(b in A)
print(A.index(b))

c = 10
print(c in A)
# print(A.index(c))  # выдает ошибку - "ValueError: 10 is not in list"
