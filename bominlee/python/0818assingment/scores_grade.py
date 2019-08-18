# second process
import string


def get_grade(scores, subject):
    g = ["A", "B", "C", "D", "F"]
    score_gap = list(range(80, -1, -20))

    for i in list(range(0, 5)):
        print(scores, i)
        if scores[subject] > score_gap[i] :
            ## 문제 이상해. 20 초과면 D학점이겠지???
            print(i)
            return g[i]


print(get_grade({'국어': 20, '영어': 50, '수학': 70}, '영어'))
