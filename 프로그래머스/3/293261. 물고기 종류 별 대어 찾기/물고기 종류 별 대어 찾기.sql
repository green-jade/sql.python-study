WITH temp
AS(
SELECT 
    ID
    , FISH_INFO.FISH_TYPE
    , FISH_NAME
    , LENGTH
    , ROW_NUMBER() OVER(PARTITION BY FISH_TYPE ORDER BY LENGTH DESC) AS 'RANK'
FROM FISH_INFO
LEFT JOIN FISH_NAME_INFO
ON FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
)
SELECT 
    ID, FISH_NAME, LENGTH
FROM 
    temp
WHERE  temp.RANK = 1
ORDER BY ID ASC

