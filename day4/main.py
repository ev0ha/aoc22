def problem1(input_data: str) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line.strip().split(",")) for line in f.readlines()]

    result = 0

    for x in data:
        l = x[0].split("-")
        r = x[1].split("-")
        left_range = range(int(l[0]), int(l[1])+1)
        right_range = range(int(r[0]), int(r[1])+1)

        left_contains_right = all(items in left_range for items in right_range)
        right_contains_left = all(items in right_range for items in left_range)

        if left_contains_right or right_contains_left:
            result += 1

    return result

def problem2(input_data: str) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line.strip().split(",")) for line in f.readlines()]

    result = 0

    for x in data:
        l = x[0].split("-")
        r = x[1].split("-")
        left_range = range(int(l[0]), int(l[1])+1)
        right_range = range(int(r[0]), int(r[1])+1)

        if all(items not in left_range for items in right_range):
            continue
        else:
            result += 1

    return result

print(problem1('input.txt'))
print(problem2('input.txt'))
