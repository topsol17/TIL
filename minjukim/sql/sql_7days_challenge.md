# 7일차 루시와 엘라 찾기
    mySQL

    SELECT i.ANIMAL_ID, i.NAME, i.SEX_UPON_INTAKE
    FROM ANIMAL_INS i
    WHERE i.NAME IN ('Lucy', 'Ella', 'Pickle', 'Sabrina', 'Rogan', 'Mitty')

WHERE 절 처음 코드

    WHERE (i.NAME = 'Lucy') OR (i.NAME = 'Ella') OR (i.NAME = 'Lucy') OR (i.NAME = 'Pickle') OR (i.NAME = 'Sabrina') OR (i.NAME = 'Rogan') OR (i.NAME = 'Mitty')

LEFT(컬럼/문자열, 숫자(정수)))

    LEFT('APPLE', 3) = 'APP'

SUBSTRING_INDEX(컬럼, ' ', 1)

    SUBSTRING_INDEX('INTACT MALE', ' ', 1) = 'INTACT
' '공백을 기준으로 잘라서 첫번째 컴포넌트 출력