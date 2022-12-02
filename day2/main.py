# 1 for Rock, 2 for Paper and 3 for Scissors
# X for Rock, Y for Paper and Z for Scissors
# X for Lose, Y for Draw  and Z for Win

player_strat = { 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }
opp = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors' }
beats = { 'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock' }

def points_for_decision(i: str) -> int:
    if i == 'Rock':
        return 1
    elif i == 'Paper':
        return 2
    else:
        return 3

def calc_points_strat_one(game: dict) -> int:
    result = 0

    for k, v in game.items():
        if opp[k] == player_strat[v]:
            result += points_for_decision(player_strat[v]) + 3
        elif beats[opp[k]] == player_strat[v]:
            result += points_for_decision(player_strat[v])
        else:
            result += points_for_decision(player_strat[v]) + 6

    return result

def calc_points_strat_two(game: dict) -> int:
    result = 0
    reversed_beats = dict((v, k) for k, v in beats.items())

    for k, v in game.items():
        if v == 'X':
            result += points_for_decision(beats[opp[k]])
        elif v == 'Y':
            result += points_for_decision(opp[k]) + 3
        else:
            result += points_for_decision(reversed_beats[opp[k]]) + 6

    return result

def common(input_data: str, calc) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line.strip().split(" ")) for line in f.readlines()]

    result = 0

    for x in data:
        item = iter(x)
        data_dct = dict(zip(item, item))
        result += calc(data_dct)

    return result

def problem1(input_data: str) -> int:
    return common(input_data, calc_points_strat_one)

def problem2(input_data: str) -> int:
    return common(input_data, calc_points_strat_two)

print(problem1('input.txt'))
print(problem2('input.txt'))
