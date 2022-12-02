from main import problem1, problem2

def test_input_simple():
    assert problem1('input_test.txt') == 24000

def test_part_two():
    assert problem2('input_test.txt') == 45000
