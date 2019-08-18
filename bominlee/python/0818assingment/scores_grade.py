# second process
import string


def grades(scores, subject):
    g = ["A", "B", "C", "D", "F"]
    score_gap = list(range(80, 0, -20))
    for score in scores:
        for i in list(range(0, 5)):
            # print(score, i)
            if score[subject] > score_gap[i] :
                ## 문제 이상해. 20 초과면 D학점이겠지???
                # print(i)
                return g[i]


print(grades([{'국어': 20, '영어': 50, '수학': 70}], '영어'))
