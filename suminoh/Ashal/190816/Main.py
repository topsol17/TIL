from scores import grade
import pandas as pd


def main():
    score = {'국어': 45, '과학': 70, '수학': 80}
    subject = []
    scores = []
    grades = []
    for i in score.keys():
        grades.append(grade(score, i))
        subject.append(i)
        scores.append(score[i])
    score_table = pd.DataFrame({'과목': subject, '점수': scores, '등급': grades})
    print(score_table)


main()
