"""
Consider a "word" as any sequence of capital letters A-Z (not limited to just "dictionary words").
For any word with at least two different letters, there are other words composed of the same letters
but in a different order (for instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words;
for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters as these two).

We can then assign a number to every word, based on where it falls in an alphabetically sorted list
of all words made up of the same group of letters. One way to do this would be to generate the entire
list of words and find the desired one, but this would be slow if the word is long.

Given a word, return its number. Your function should be able to accept any word 25 letters or
less in length (possibly with some letters repeated), and take no more than 500 milliseconds to run.
To compare, when the solution code runs the 27 test cases in JS, it takes 101ms.

For very large words, you'll run into number precision issues in JS (if the word's position
is greater than 2^53). For the JS tests with large positions, there's some leeway (.000000001%).
If you feel like you're getting it right for the smaller ranks, and only failing by rounding on
the larger, submit a couple more times and see if it takes.

Python, Java and Haskell have arbitrary integer precision, so you must be precise
in those languages (unless someone corrects me).

C# is using a long, which may not have the best precision, but the tests are locked so we can't change it.

Sample words, with their rank:
ABAB = 2
AAAB = 1
BAAA = 4
QUESTION = 24572
BOOKKEEPER = 10743
"""


def factorial(i):
    if i == 1:
        return 1
    else:
        fact = 1
        for counter in range(1, i + 1):
            fact *= counter
        return fact


def string_to_dict(string):
    string_dict = dict()
    for i in string:
        if i in string_dict:
            string_dict[i] += 1
        else:
            string_dict[i] = 1
    return string_dict


def dict_to_factorial(string_dict):
    dict_factorial = 1
    for i in string_dict:
        dict_factorial *= factorial(string_dict[i])
    return dict_factorial


def listPosition(word):
    """Возвращает номер перестановки данной строки
    Return the anagram list position of the word"""
    sort_word = sorted(word)
    len_word = len(sort_word)
    position = 1
    word_dict = string_to_dict(word)

    for i in word:
        dict_factorial = dict_to_factorial(word_dict)
        position += (sort_word.index(i) * factorial(len_word-1) // dict_factorial)
        word_dict[i] -= 1
        len_word -= 1
        sort_word.remove(i)

    return position


print(listPosition('IMMUNOELECTROPHORETICALLY'))
print(718393983731145698173)

"""
print(listPosition('ABAB'))
print(listPosition('ABAB') == 2)

print(listPosition('QUESTION'))
print(listPosition('QUESTION') == 24572)


print(listPosition('BOOKKEEPER'))
print(listPosition('BOOKKEEPER') == 10743)

print(listPosition('AABA'))
print(listPosition('AABA') == 2)

print(listPosition('FCEBAD') == 669)
"""
