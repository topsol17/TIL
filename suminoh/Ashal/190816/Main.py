from scores import grade


def main():
    score = {'국어': 45, '과학': 70, '수학': 80}
    print('국어 : ', grade(score, '국어'))
    print('과학 : ', grade(score, '과학'))
    print('수학 : ', grade(score, '수학'))


main()
