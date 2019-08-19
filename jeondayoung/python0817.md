# Python Basic 19.08.16

## 조건 분기
```python
if score >= 50:
  high_scores.append(score)
```
**둘 중 작은 숫자 찾기**
```python
# 1. Test-first
def test_less_number():
    assert less_number(10, 20) == 10
    assert less_number(30, 20) == 20


# 2. Implement
def less_number(number1, number2):
    if number1 < number2:
        return number1
    return number2
# return number2가 핵심 (없으면, y값을 인지못하고 오류가 난다)
```
**50점 이상 점수 찾기**
```python
# 1. Test-first
def test_select_high_scores():
    assert select_high_scores([], 50) == []
    assert select_high_scores([60], 50) == [60]
    assert select_high_scores([60, 40], 50) == [60]
    assert select_high_scores([60, 40, 50], 50) == [60, 50]
    assert select_high_scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 50) == \
           [50, 60, 70, 80, 90, 100]


# 2. Implement
def select_high_scores(scores, pivot):
    # Initial accumulator
    high_scores = []

    # Accumulation
    for score in scores:
        # Conditional
        if score >= pivot:
            high_scores.append(score)

    # Return
    return high_scores
```

----------------------------------
## 삼항연산
**둘 중 작은 숫자 찾기**
```python

# 1. Test-first
def test_less_number():
    assert less_number(10, 20) == 10
    assert less_number(20, 10) == 10


# 2. Implement
def less_number(x, y):
    return x < y and x or y
```
----------------------------------------------
# Python 연습문제 
## 1. 20점 단위 A-F 학점으로 분류하시오. ( A: 100-80 / B: 80-60 / c:60-40 / D:40-20 / F:20-0)
## 2. 테이블로 표시하시오.

> class_scores = [{'국어':80, '영어': 100, '수학':50},{'국어':90, '영어': 70, '수학;:40}]

```python
def test_a_group_score():
    assert scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [80, 90, 100]
    assert scores([10, 20, 30, 40, 50, 60, 70, 80, 100]) == [80, 100]

def test_b_group_score():
    assert scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [60, 70, 80]
    assert scores([10, 20, 30, 40, 50, 70, 80, 100]) == [70, 80]

def test_c_group_score():
    assert scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [40, 50, 60]
    assert scores([10, 20, 30, 50, 60, 70, 80, 100]) == [50, 60]

def test_d_group_score():
    assert scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [20, 30, 40]
    assert scores([10, 20, 40, 50, 60, 70, 80, 100]) == [20, 40]

def test_f_group_score():
    assert scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 20]
    assert scores([10, 30, 40, 50, 60, 70, 80, 100]) == [10]


def a_group_score(scores):
    a_scores = []
    for a in scores:
        if a >= 80 & a <= 100:
            a_scores.append(a)
    return a_scores

def b_group_score(scores):
    b_scores = []
    for b in scores:
        if b >= 60 & b <= 80:
            b_scores.append(b)
    return b_scores


def c_group_score(scores):
    c_scores = []
    for c in scores:
        if c >= 40 & c <= 60:
            c_scores.append(c)
    return c_scores

def d_group_score(scores):
    d_scores = []
    for d in scores:
        if d >= 20 & d <= 40:
            d_scores.append(d)
    return d_scores

def f_group_score(scores):
    f_scores = []
    for f in scores:
        if f >= 0 & f <= 20:
            f_scores.append(f)
    return f_scores
```
이렇게 A,B,C,D,F 별로 그룹나눠서 점수 구분하는 건 했는데, 테이블로 보여주는거랑 과목명 넣는걸 도저히 못하겠어요ㅠㅠㅠ