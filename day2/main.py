# 1 for Rock, 2 for Paper, and 3 for Scissors
# X for Rock, Y for Paper, and Z for Scissors

player = { 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }
opp = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors' }
beats = { 'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock' }

def points_for_decision(i: str) -> int:
    if i == player['X']:
        return 1
    elif i == player['Y']:
        return 2
    else:
        return 3

def calc_points(game: dict) -> int:
    result = 0

    for k, v in game.items():
        if opp[k] == player[v]:
            result += points_for_decision(player[v]) + 3
        elif beats[opp[k]] == player[v]:
            result += points_for_decision(player[v])
        else:
            result += points_for_decision(player[v]) + 6

    return result

def problem1(input_data: str) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line.strip().split(" ")) for line in f.readlines()]

    result = 0
    for x in data:
        item = iter(x)
        data_dct = dict(zip(item, item))
        result += calc_points(data_dct)

    return result

def problem2(input_data: str) -> int:
    return

print(problem1('input.txt'))
