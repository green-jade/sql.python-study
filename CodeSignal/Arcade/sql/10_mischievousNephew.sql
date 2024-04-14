'''
The resulting table should contain four columns, weekday, mischief_date, author, and title, where weekday is the weekday of mischief_date (0 for Monday, 1 for Tuesday, and so on, with 6 for Sunday). The table should be sorted by the weekday column, and for each weekday Huey\'s mischief should go first, Dewey\'s should go next, and Louie\'s should go last. In case of a tie, mischief_date should be a tie-breaker. If there\'s still a tie, the record with the lexicographically smallest title should go first.
'''
-- WEEKDAY() 와 DAYOFWEEK() 함수 차이 : WEEKDAY()는 월요일부터 0~6, DAYOFWEEK()는 일요일부터 1~7

-- ORDER BY 와 CASE WHEN을 같이 쓰는 방법
CREATE PROCEDURE solution()
BEGIN
	SELECT WEEKDAY(mischief_date) AS weekday,mischief_date,author,title
	FROM mischief
	ORDER BY weekday,
		CASE WHEN author = 'Huey' THEN 1
			WHEN author = 'Dewey' THEN 2
			WHEN author = 'Louie' THEN 3
		END,
		mischief_date, title;
		
END

-- FIELD() 함수 쓰는 방법 
CREATE PROCEDURE solution()
BEGIN
	SELECT WEEKDAY(mischief_date) AS weekday,mischief_date,author,title
	FROM mischief
	ORDER BY weekday, FIELD(author,'Huey','Dewey','Louie'),
		mischief_date, title;
		
END