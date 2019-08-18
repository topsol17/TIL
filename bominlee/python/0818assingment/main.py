import pandas as pd
from scores_grade import get_grade


def main():
    class_scores = [
        {'Name': 'Jane', 'Korean': 80, 'English': 100, 'Math': 50},
        {'Name': 'Brown', 'Korean': 90, 'English': 70, 'Math': 40}
    ]

    class_grades = class_scores.copy()

    for scores in class_grades:
        for subject in ['Korean', 'English', 'Math']:
            scores[subject] = get_grade(scores, subject)

    table = pd.DataFrame(class_grades, columns=['Name', 'Korean', 'English', 'Math'])

    return print(table)


main()
