import pandas as pd

#'국어': 80, '영어': 100, '수학': 50}, {'국어': 90, '영어': 70, '수학': 40}

#손으로 직접 입력한 데이터...work1에서 값을 빼서 오고 싶다...그럴려면...work1에서 데이터 값을 받야하는데...
df = pd.DataFrame(data={'subject': ['국어','영어', '수학'], 'score': [80, 100, 50], 'grade': ['A', 'A', 'C']})
print(df)

#테이블 컬럼
'''fmt = [
    ('subject',       'subject',   8),
    ('score',          'score',       8),
    ('grade', 'grade', 8),
]

#테이블 내용
data = [
    {'subject':'국어', 'score':'80', 'grade':'A'},
    {'subject': '영어', 'score': '100', 'grade': 'A'},
    {'subject': '수학', 'score': '50', 'grade': 'C'},
    {'subject': '국어', 'score': '90', 'grade': 'A'},
    {'subject': '영어', 'score': '70', 'grade': 'B'},
    {'subject': '수학', 'score': '40', 'grade': 'C'}
]

print(TablePrinter(fmt)(data) )'''