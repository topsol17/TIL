def grade(scores, subject):
    if scores[subject] >= 80:
        return 'A'
    elif scores[subject] >= 60:
        return 'B'
    elif scores[subject] >= 40:
        return 'C'
    elif scores[subject] >= 20:
        return 'D'
    else:
        return 'F'
