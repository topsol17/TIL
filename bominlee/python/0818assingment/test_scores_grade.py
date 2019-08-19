## testcase first

from scores_grade import get_grade

def test_scores_grade():
    assert get_grade({'국어': 100}, '국어') == "A"
    assert get_grade({'국어': 79, '영어': 50, '수학': 10}, '국어') == "B"
    assert get_grade({'국어': 20, '영어': 50, '수학': 70}, '영어') == "C"
    assert get_grade({'국어': 20, '영어': 50, '수학': 39}, '수학') == "D"
    assert get_grade({'국어': 20, '영어': 50, '수학': 0}, '수학') == "F"
    # 100~80 A, 79~60 B, 59~40 C, 39 ~ 20 D, 19 ~ 0 F
