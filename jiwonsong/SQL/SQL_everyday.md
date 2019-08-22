# SQL everyday 문제풀이
## LeetCode
```SQL
# 596. Classes More Than 5 Students

    SELECT class
    FROM courses
    GROUP BY class
    HAVING COUNT(DISTINCT student) >= 5
    ;

# 595. Big Countries

    SELECT name, population, area
    FROM world
    WHERE area >= 3000000 OR population >= 25000000
    ;

# 620. Not Boring Movies

    SELECT *
    FROM cinema
    WHERE mod(id,2) = 1
    AND description != ('boring')
    ORDER BY rating DESC
    ;

# 197. Rising Temperature

    SELECT weather.id AS 'Id'
    FROM weather a JOIN weather b ON DATEDIFF(a.date, b.date) = 1
    AND a.Temperature > b.Temperature
    ;

# 184. Department Highest Salary

    SELECT
        Department.name AS 'Department',
        Employee.name AS 'Employee',
        Salary
    FROM
        Employee
            JOIN
        Department ON Employee.DepartmentId = Department.Id
    WHERE
        (Employee.DepartmentId , Salary) IN
        (   SELECT
                DepartmentId, MAX(Salary)
            FROM
                Employee
            GROUP BY DepartmentId
    	)
    ;

# 180. Consecutive Numbers

    SELECT *
    FROM
        Logs l1,
        Logs l2,
        Logs l3
    WHERE
        l1.Id = 12.Id - 1
        AND l2.Id = l3.Id -1
        AND l1.Num = l2.Num
        AND l2.Num = l3.Num
    ;
    
```
## HackerRank
```SQL
# Type of Triangle

    SELECT  CASE
       WHEN A+B>C AND B+C>A AND A+C>B THEN
           CASE
               WHEN A=B AND B=C THEN 'Equilateral'
               WHEN A=B or A=C OR B=C THEN 'Isosceles'
               ELSE 'Scalene'
           END
       ELSE 'Not A Triangle'
    END
    FROM TRIANGLES
```
