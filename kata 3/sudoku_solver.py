"""
Write a function that will solve a 9x9 Sudoku puzzle.
The function will take one argument consisting of
the 2D puzzle array, with the value 0 representing
an unknown square.

The Sudokus tested against your
function will be "easy" (i.e. determinable;
there will be no need to assume and test
possibilities on unknowns) and can be
solved with a brute-force approach.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]
"""

def get_list(puzzle, y, x):
    """получение трех списков для сравнения"""
    row = puzzle[y]
    columns = [i[x] for i in puzzle]
    square = []

    """получение списка из соответствующего квадрата"""
    add_i = {0: 0,
             1: 0,
             2: 0,
             3: 3,
             4: 3,
             5: 3,
             6: 6,
             7: 6,
             8: 6,
             }
    add_j = {0: 0,
             1: 0,
             2: 0,
             3: 3,
             4: 3,
             5: 3,
             6: 6,
             7: 6,
             8: 6,
             }
    for j in range(3):
        for i in range(3):
            square.append(puzzle[j+add_j[y]][i+add_i[x]])

    return row, columns, square


def find_to_insert(puzzle, y, x, start_find):
    """нахождение числа, которое можно вставить
     в клетку puzzle[y][x], которое соответствовало бы
     правилам судоку"""
    puzzle = puzzle
    y = y
    x = x

    """получение трех списков для сравнения"""
    row, columns, square = get_list(puzzle, y, x)

    """находим наименьшее число от 1 до 9, которое
    не находися в трех вышеполученных списках.
    если такое число найдено, то его возвращаем"""
    for count in range(start_find, 10):
        if count not in row and count not in columns and count not in square:
            return count

    return False


def sudoku(puzzle):
    puzzle = puzzle

    """создаем вспомогательный список,
    в котором будут хранится списки из трех значений
    координаты вставленного числа и само число
    """
    help_list = [[0, 0, 0]]
    """число со старта которого начинается поиск"""
    start_find = 1

    y = 0
    while y < 9:
        x = 0
        while x < 9:
            """если в клетке ноль, то вызываем функцию
            поиска числа, которое можно вставить в эту клетку"""
            if not puzzle[y][x]:
                count = find_to_insert(puzzle, y, x, start_find)
                if count:
                    puzzle[y][x] = count
                    help_list.append([x, y, count])
                    start_find = 1
                    x += 1
                else:
                    """help_list уже не пустой, так как должно было
                    вставится хоть одно значение в первую пустую ячейку"""
                    x = help_list[-1][0]
                    y = help_list[-1][1]
                    start_find = help_list[-1][2] + 1
                    puzzle[y][x] = 0
                    help_list.pop()
            else:
                x += 1
        y += 1

    return puzzle


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

x = sudoku(puzzle)
for i in x:
    print(i)

print(sudoku(puzzle) == solution)


puzzle = [[0, 0, 0, 0, 0, 5, 0, 0, 0],
          [4, 0, 0, 0, 0, 0, 8, 0, 0],
          [0, 0, 8, 2, 0, 3, 0, 6, 0],
          [0, 0, 0, 0, 9, 0, 0, 0, 0],
          [0, 7, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 4, 6, 0, 8, 0, 3, 0],
          [0, 0, 2, 0, 5, 0, 0, 0, 0],
          [0, 0, 0, 0, 4, 0, 0, 9, 0],
          [1, 0, 0, 9, 0, 2, 0, 0, 3]]

x = sudoku(puzzle)
for i in x:
    print(i)
