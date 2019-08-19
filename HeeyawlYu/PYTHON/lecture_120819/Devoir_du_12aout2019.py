# class_scores = [
#     {
#         '국어': 80,
#         '영어': 100,
#         '수학': 50
#     },
#     {
#         '국어': 90,
#         '영어': 70,
#         '수학': 40
#     }
# ]


# 1) 두 개의 dictionary에서 국어 점수의 총 합은?

# def test_class_total():
#     assert class_total(askfjkl)


def test_scores():
    scores = [10, 20, 30]

    #
    acc = 0

    #
    acc += scores[0]
    acc += scores[1]
    acc += scores[2]

    for i in [0, 1, 2]:
        acc += scores[i]


def test_for():
    print()

    for i in [0, 1, 2]:
        print(i)

    # print(0)
    # print(1)
    # print(2)


def test_class_scores():
    class_scores = [
        {'국어': 10, '영어': 20},
        {'국어': 60, '영어': 80},
    ]

    assert class_scores[0] == {'국어': 10, '영어': 20}
    assert class_scores[0] == {'영어': 20, '국어': 10}

    print(class_scores[0])
    print(class_scores[1])


def test_set():
    print('\n\n**** test_set')
    assert {1, 2, 3, 4, 1} == {1, 2, 4, 3}
    assert len({1, 2, 3, 4, 1}) == 4
    # assert {1, 2, 3, 4}[1] == 1
    assert {'국어': 1}['국어'] == 1
    assert {'국어': '국어'}['국어'] == '국어'
    # assert {'국어'}['국어'] == '국어'
    assert '국어' in {'국어'}
    for i in {'영어', '국어', '국어'}:
        # assert i == '국어'
        print(i)
    print('***')
    for i in ['영어', '국어', '국어']:
        # assert i == '국어'
        print(i)


# print(class_scores)

# => assert class_total(class_scores, '국어') == 170
# 이렇게 확인할 수 있는 함수를 만들어보세요
#
# 2) class_scores set에 있는 모든 점수의 합은 얼마인가요? 역시 함수를 만들어보세요
#
# => assert class_total_all(class_scores) == 430


# def test_double():
#     assert double(1) == 2
#     assert double(2) == 4


def add(x, y):
    return x + y


def test_add():
    assert add(3, 4) == 7
    assert add(4, 4) == 8
    assert add(4, 10) == 14
    a = 3
    b = 4
    assert add(a, b) == 7
    assert add(3, b) == 7
    assert add(3, 4) == 7


def class_total(class_scores, subject):
    pass


def test_class_total_sample():
    assert class_total([], '국어') == 0
    # assert class_total([
    #     {0: 80}
    # ], 0) == 80
    # assert class_total([
    #     {'국어': 80}
    # ], '국어') == 80
    # assert class_total([
    #     {'국어': 80},
    #     {'국어': 90}
    # ], '국어') == 170
    # assert class_total([
    #     {
    #         '국어': 80,
    #         '영어': 100,
    #         '수학': 50
    #     },
    #     {
    #         '국어': 90,
    #         '영어': 70,
    #         '수학': 40
    #     }
    # ], '국어') == 170
