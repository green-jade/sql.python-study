-- 코드를 작성해주세요
SELECT id,
CASE WHEN size_of_colony<=100 THEN 'LOW'
WHEN size_of_colony>100 AND size_of_colony<=1000 THEN 'MEDIUM'
WHEN size_of_colony>1000 THEN 'HIGH' END AS 'SIZE'
FROM ECOLI_DATA
ORDER BY ID ASC