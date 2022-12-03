from functools import reduce


def char_range(char1: str, char2: str):
    for c in range(ord(char1), ord(char2)+1):
        yield chr(c)

chars = []

for c in char_range('a', 'z'):
    chars.append(c)
for c in char_range('A', 'Z'):
    chars.append(c)

charNumbers = { chars[i] : i+1 for i in range(0, len(chars) ) }

def problem1(input_data: str) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line.strip()) for line in f.readlines()]

    result = []

    for x in data:
        str1 = x[:len(x)//2]
        str2 = x[len(x)//2:]
        x = set(str1) & set(str2)
        result.append(charNumbers[list(x)[0]])

    result = reduce((lambda x, y: x + y), result, 0)

    return result

def problem2(input_data: str) -> int:
    data = []

    with open(input_data) as f:
        [data.append(line.strip()) for line in f.readlines()]

    bagsOfThree = []

    for i in range(0, len(data)-1, 3):
        group = []
        for x in range(0, 3):
            group.append(data[i+x])
        bagsOfThree.append(group)

    result = []

    for x in bagsOfThree:
        badge = set(x[0]) & set(x[1]) & set(x[2])
        result.append(charNumbers[list(badge)[0]])

    result = reduce((lambda x, y: x + y), result, 0)

    return result

print(problem1('input.txt'))
print(problem2('input.txt'))
