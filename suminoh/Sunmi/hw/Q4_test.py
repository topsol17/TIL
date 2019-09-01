from Q4_mode import mode


def test_mode():
    assert mode([1]) == 1
    assert mode([1, 2, 3, 3]) == 3
    assert mode([1, 2]) == [1, 2]
    assert mode([1, 2, 2, 3, 3]) == [2, 3]


test_mode()
