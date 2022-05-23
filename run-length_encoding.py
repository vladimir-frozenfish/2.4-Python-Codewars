def run_length_encoding(s):
    if not s:
        return []

    archive = [[1, s[0]]]

    for char in s[1:]:
        if char == archive[-1][1]:
            archive[-1][0] += 1
        else:
            archive.append([1, char])

    return archive

print(run_length_encoding(''))
print(run_length_encoding('hello world!'))

