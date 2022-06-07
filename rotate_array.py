def rotate(data, n):
    len_data = len(data)
    if len_data < 2:
        return data

    sdvig = n % len_data
    return data[len_data - sdvig:] + data[:len_data - sdvig]


print(rotate([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4])
print(rotate([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1])
print(rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3])
print(rotate([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2])
print(rotate([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2])
print(rotate([1, 2, 3, 4, 5], -3) == [4, 5, 1, 2, 3])
print(rotate([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1])
print(rotate([1, 2, 3, 4, 5], -4) == [5, 1, 2, 3, 4])
print(rotate([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5])
print(rotate([1, 2, 3, 4, 5], -5) == [1, 2, 3, 4, 5])
print(rotate([1, 2, 3, 4, 5], 6) == [5, 1, 2, 3, 4])
print(rotate([1, 2, 3, 4, 5], -6) == [2, 3, 4, 5, 1])
print(rotate([True, True, False], 2) == [True, False, True])
print(rotate([1, 2, 3, 4, 5], 12478) == [3, 4, 5, 1, 2])
print(rotate([], 976999) == [])