'''
According to school policy, there are three possible ways to evaluate a grade:

Option 1: Grade = 0.25 * Midterm1 + 0.25 * Midterm2 + 0.5 * Final;
Option 2: Grade = 0.5 * Midterm1 + 0.5 * Midterm2;
Option 3: Grade = Final.
Each student\'s final grade comes from the option that works the best for that student.

query the name and id of all the students whose best grade comes from Option 3, sorted based on the first 3 characters of their name. If the first 3 characters of two names are the same, then the student with the lower ID value comes first.
'''
-- first 3 characters of name : LEFT(Name,3)으로 구현
-- 직접 연산한 값으로 비교하는 방법
CREATE PROCEDURE solution()
BEGIN
	SELECT Name,ID
	FROM Grades
	WHERE Final > Midterm1*.25+Midterm2*.25+Final*.5 
	ORDER BY LEFT(Name,3),ID;
	
END

-- 서브쿼리 만들어서 같은 행의 값끼리 비교하는 방법
-- 같은 행 내에서는 max/min연산이 안됨에 유의하자
CREATE PROCEDURE solution()
BEGIN
    SELECT t.name as Name, t.ID as ID
    FROM (
        SELECT name, ID, 
        (Midterm1 * 25 / 100) + (Midterm2 * 25 / 100) + (Final * 50/100) as option_1,
        (Midterm1 * 50 / 100) + (Midterm2 * 50 / 100) as option_2,
        Final as option_3
        FROM Grades
        ) t
    WHERE t.option_3 > t.option_2 and t.option_3 > t.option_1
    ORDER by LEFT(name,3) asc, ID ASC ;
END