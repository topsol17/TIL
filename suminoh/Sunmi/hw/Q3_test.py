from Q3_median import median


def test_median():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 3, 7, 5]) == 4
    assert median([9, 3, 5, 5, 4]) == 5


test_median()