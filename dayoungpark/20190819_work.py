# 20190819 파이썬 과제
# 20점 단위로 A-F 학점, 테이블 출력.

class_scores = [{'국어': 80, '영어': 100, '수학': 50}, {'국어': 90, '영어': 70, '수학': 40}]

def grade(scores):
    if scores >= 80:
        return 'A'
    elif scores >= 60:
        return 'B'
    elif scores >= 40:
        return 'C'
    elif scores >= 20:
        return 'D'
    else:
        return 'F'

def test_grade_scores():
    assert grade(80) == 'A'
    assert grade(60) == 'B'
    assert grade(40) == 'C'
    assert grade(20) == 'D'
    assert grade(10) == 'F'
    assert grade(100) == 'A'

# 각 과목별의 점수를 어디에 저장해서 출력하고 싶은데..어떻게 해야할까...밑에 있는 코드를 어떻게 활용하면 될 꺼 같은데..
'''def grade_scores(class_scores, subject):
    for i in range(len(class_scores)):
        scores = class_scores[i]
        total_score += scores[subject]
    return total_score'''