# Prepare input with awk; Examples below with test inputs
#
# Use awk to split input file on empty line, producing two files
# "input_test_1" containing the stacks
# "input_test_2" containing the moves
# awk -v RS= '{print > ("input_test_" NR ".txt")}' input_test.txt
#
# Replace whitespaces in stacks with "0" from input_test_1.txt, producing input_test_stacks.txt
# awk '{gsub(/[[:blank:]]/,"0"); print}' input_test_1.txt | cat > input_test_stacks.txt
#
# Further clean up input_test_stacks.txt
# awk '{gsub( "[[]","" ); gsub( "[]]","" ); gsub( "0{4}","-"); gsub( "0{1,3}","" ); print}' input_test_stacks.txt
# | cat > input_test_stacks_clean.txt
#
# Clean up input_test_2.txt to input_test_moves_clean.txt
# awk '{gsub( /move /,""); gsub( / from /,"-" ); gsub( / to /,"-" ); print}' input_test_2.txt
# | cat > input_test_moves_clean.txt

def common_prep(input_stacks: str, input_moves: str) -> tuple:
    data_stacks = []
    data_stacks_clean = []
    data_moves = []
    data_moves_clean = []

    with open(input_stacks) as f:
        [data_stacks.append(line.strip()) for line in f.readlines()]
    with open(input_moves) as f:
        [data_moves.append(line.strip()) for line in f.readlines()]

    # Works for stacks < 10, if stacks bigger then: number_of_stacks = int(data_stacks[-1]) % 10
    number_of_stacks = len(data_stacks[-1])

    for x in range(0, number_of_stacks):
        data_stacks_clean.append([])

    for x in data_stacks:
        clean_x = list(x)
        i = 0
        for y in clean_x:
            if y.isalpha():
                data_stacks_clean[i].append(y)
                i += 1
            else:
                i += 1
    for x in data_moves:
        data_moves_clean.append(x.split("-"))

    return (data_stacks_clean, data_moves_clean)

def common_result(data_stacks: str) -> str:
    result = []

    for x in data_stacks:
        if not x:
            continue
        else:
            result.append(x[0])

    result = ''.join(result)

    return result

def problem1(input_stacks: str, input_moves: str) -> str:
    data_stacks_clean, data_moves_clean = common_prep(input_stacks, input_moves)

    for x in data_moves_clean:
        from_stack = int(x[1])-1
        to_stack = int(x[2])-1
        sample = data_stacks_clean[from_stack][:int(x[0])]
        data_stacks_clean[from_stack] = data_stacks_clean[from_stack][int(x[0]):]
        for y in sample:
            data_stacks_clean[to_stack] = list(y) + data_stacks_clean[to_stack]

    result = common_result(data_stacks_clean)

    return result

def problem2(input_stacks: str, input_moves: str) -> str:
    data_stacks_clean, data_moves_clean = common_prep(input_stacks, input_moves)

    for x in data_moves_clean:
        from_stack = int(x[1])-1
        to_stack = int(x[2])-1
        sample = data_stacks_clean[from_stack][:int(x[0])]
        # Only difference to Problem 1 is the line below
        sample.reverse()
        data_stacks_clean[from_stack] = data_stacks_clean[from_stack][int(x[0]):]
        for y in sample:
            data_stacks_clean[to_stack] = list(y) + data_stacks_clean[to_stack]

    result = common_result(data_stacks_clean)

    return result

print(problem1('input_stacks_clean.txt', 'input_moves_clean.txt'))
print(problem2('input_stacks_clean.txt', 'input_moves_clean.txt'))

