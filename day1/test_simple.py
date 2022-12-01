from main import mostCal, threeMostCal

def test_input_simple():
    assert mostCal('input_test.txt') == 24000

def test_part_two():
    assert threeMostCal('input_test.txt') == 45000
