# second process


def get_grade(scores, subject):
    grades = {"A": 80, "B": 60, "C": 40, "D": 20, "F": 0}

    for key, value in grades.items():
        print(scores, key, value)
        if scores[subject] >= value:
            print(key)
            return key


print(get_grade({'국어': 20, '영어': 50, '수학': 70}, '영어'))
