def find_reverse_number(n):
    """поиск n-го числа с зеркальным отображением
    функция проходится последовательно по каждому такому числу,
    пока не дойдет до n-го"""

    first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if n < 11:
        return first[n - 1]

    count = 11

    add_number = 1
    temp_add_number = 1
    next_phase = 10

    while True:
        """первая фаза"""
        while add_number != next_phase:
            if count == n:
                number = int(str(add_number) + str(add_number)[-1::-1])
                return number
            count += 1
            add_number += 1

        """вторая фаза"""
        for j in range(temp_add_number, add_number):
            for i in range(0, 10):
                if count == n:
                    number = int(str(j) + str(i) + str(j)[-1::-1])
                    return number
                count += 1

        temp_add_number = add_number
        next_phase *= 10


def find_reverse_number_two(n):
    """поиск n-го числа с зеркальным отображением
    функция перестраиавет число n для получени соответствующего
    зеркального числа"""

    first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    if n < 20:
        return first[n - 1]

    insert = {
        '1': '9',
        '2': '1',
        '3': '2',
        '4': '3',
        '5': '4',
        '6': '5',
        '7': '6',
        '8': '7',
        '9': '8'
    }

    number = str(n)

    if number[0] == '1':
        if number[1] == '0':
            number_reverse = int(insert[number[0]] + number[2:] + number[-2:1:-1] + insert[number[0]])
        else:
            number_reverse = int(number[1:] + number[-1:0:-1])
        return number_reverse

    number_reverse = int(insert[number[0]] + number[1:] + number[-2:0:-1] + insert[number[0]])
    return number_reverse


print(find_reverse_number(148599))
print(find_reverse_number_two(148599))

