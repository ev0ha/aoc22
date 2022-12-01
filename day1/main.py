from functools import reduce

def mostCal(input_data: str):
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
        r = reduce((lambda a, b: a + b), x, 0)
        result.append(r)

    return max(result)


def threeMostCal(input_data: str):
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

    result = sorted(result)
    result.reverse()
    result = reduce((lambda x, y: x + y), result[:3], 0)

    return result

print(mostCal('input.txt'))
print(threeMostCal('input.txt'))

