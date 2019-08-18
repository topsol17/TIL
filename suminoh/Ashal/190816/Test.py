from scores import grade


def test_grade():
    assert grade({'국어': 0, '과학': 0, '수학': 0}, '국어') == 'F'
    assert grade({'국어': 0, '과학': 0, '수학': 0}, '과학') == 'F'
    assert grade({'국어': 0, '과학': 0, '수학': 0}, '수학') == 'F'
    assert grade({'국어': 80, '과학': 40, '수학': 90}, '국어') == 'A'
    assert grade({'국어': 80, '과학': 40, '수학': 90}, '과학') == 'C'
    assert grade({'국어': 80, '과학': 40, '수학': 90}, '수학') == 'A'


score = {'국어': 45, '과학': 70, '수학': 80}
