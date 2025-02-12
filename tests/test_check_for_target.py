from solutions.check_for_target import check_for_target

def test_true():
    assert check_for_target([1, 2, 4, 6, 8, 9, 14, 15], 13) == True

def test_false():
    assert check_for_target([1, 2, 4, 6, 8, 9, 14, 15], 30) == False