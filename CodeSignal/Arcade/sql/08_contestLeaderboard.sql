'''
leaderboard에서 select names whose scores are in 4th~8th places inclusive, sorted in descending order of their places 
'''

-- using LIMIT #,#
CREATE PROCEDURE solution()
BEGIN
	SELECT name FROM leaderboard 
	ORDER BY score DESC 
	LIMIT 3,5;
END

-- using LIMIT and OFFSET
CREATE PROCEDURE solution()
BEGIN
	SELECT name FROM leaderboard 
    ORDER BY score DESC 
    LIMIT 5 OFFSET 3;
END


-- using window function : RANK()
CREATE PROCEDURE solution()
BEGIN
    SELECT name
    FROM(
        SELECT name, RANK() 
        OVER (ORDER BY score DESC) AS ranking
        FROM leaderboard    
    ) AS lb
    WHERE ranking BETWEEN 4 AND 8;
END