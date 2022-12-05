from main import problem1, problem2

def test_problem1():
    assert problem1('input_test_stacks_clean.txt', 'input_test_moves_clean.txt') == 'CMZ'

def test_problem2():
    assert problem2('input_test_stacks_clean.txt', 'input_test_moves_clean.txt') == 'MCD'
