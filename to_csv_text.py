def to_csv_text(array):
    result = ''
    for string in array:
        result += ','.join(list(map(str, string))) + '\n'
    return result.rstrip('\n')

print(to_csv_text([
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]
        ]))