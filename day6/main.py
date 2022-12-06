def common(input_data: str, distinct_chars: int) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line) for line in f.readlines()]
        data = ''.join(data)

    x = 0
    y = distinct_chars
    diff_chars = False
    result = 0

    while not diff_chars:
        subs = data[x:y]
        if len(set(subs)) == distinct_chars:
            result = y
            diff_chars = True
        x += 1
        y += 1

    return result

def problem1(input_data: str) -> int:
    return common(input_data, 4)

def problem2(input_data: str) -> int:
    return common(input_data, 14)

print(problem1('input.txt'))
print(problem2('input.txt'))
