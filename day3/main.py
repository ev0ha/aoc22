from functools import reduce


def char_range(char1, char2):
    for c in range(ord(char1), ord(char2)+1):
        yield chr(c)

chars = []

for c in char_range('a', 'z'):
    chars.append(c)
for c in char_range('A', 'Z'):
    chars.append(c)

charNumbers = { chars[i] : i+1 for i in range(0, len(chars) ) }

def problem1(input_data: str):
    data = []

    with open(input_data) as f:
        [data.append(line.strip()) for line in f.readlines()]

    result = []

    for x in data:
        str1 = x[:len(x)//2]
        str2 = x[len(x)//2:]
        x = set(str1)&set(str2)
        result.append(charNumbers[list(x)[0]])

    result = reduce((lambda x, y: x + y), result, 0)

    return result

def problem2():
    return

print(problem1('input.txt'))
