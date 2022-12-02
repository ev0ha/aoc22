from functools import reduce

def common(input_data: str):
    input = []

    with open(input_data) as f:
        [input.append(int(line.strip() or 0)) for line in f.readlines()]

    foodGrouped = [[]]

    i = 0

    for x in input:
        if x != 0:
            foodGrouped[i].append(x)
        else:
            foodGrouped.append([])
            i += 1

    result = []

    for x in foodGrouped:
        r = reduce((lambda x, y: x + y), x, 0)
        result.append(r)

    return result

def problem1(input_data: str):
    result = common(input_data)

    return max(result)


def problem2(input_data: str):
    result = common(input_data)
    result = sorted(result)
    result.reverse()
    result = reduce((lambda x, y: x + y), result[:3], 0)

    return result

print(problem1('input.txt'))
print(problem2('input.txt'))

