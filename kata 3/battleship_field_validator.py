"""
Write a method that takes a field for well-known board game
"Battleship" as an argument and returns true if it has a
valid disposition of ships, false otherwise.
Argument is guaranteed to be 10*10 two-dimension array.
Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships"
and objective is to destroy enemy's forces by targetting individual
cells on his field. The ship occupies one or more cells in the grid.
Size and number of ships may differ from version to version.
In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board
and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells),
2 cruisers (size 3), 3 destroyers (size 2) and
4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
"""


def validate_battlefield(field):
    """дополнение в поле дополнительных полей по периметру"""
    battle_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    battle_field += field + [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(len(battle_field)):
        battle_field[i].insert(0, 0)
        battle_field[i].append(0)

    quantity_battle = 0
    quantity_battle_four = 10

    """цикл проверки клеток"""
    for j in range(1, 12):
        for i in range(1, 12):
            if battle_field[j][i] == 1:
                """если по диагонали есть корабль, что неправильно, 
                возвращается False"""
                if (battle_field[j-1][i-1]
                        + battle_field[j-1][i+1]
                        + battle_field[j+1][i-1]
                        + battle_field[j+1][i+1] != 0):
                    return False

                quantity_battle += 1
                if battle_field[j-1][i] or battle_field[j][i-1]:
                    battle_field[j][i] = battle_field[j-1][i] + battle_field[j][i-1] + 1
                    quantity_battle_four += battle_field[j][i]

    if quantity_battle == 20 and quantity_battle_four == 35:
        return True

    return False


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))

# test.assert_equals(validate_battlefield(battleField), True, "Yep! Seems alright", "Nope, something is wrong!");