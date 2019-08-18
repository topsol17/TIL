def grade(scores, subject, grades):
    for [i, j] in [[80, 'A'], [60, 'B'], [40, 'C'], [20, 'D'], [0, 'F']]:
        if scores[subject] >= i:
            grades.append(j)
            return grades
