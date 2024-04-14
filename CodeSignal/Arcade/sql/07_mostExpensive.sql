'''
finding the product on which he spent the largest amount of money. If there are products that cost the same amount of money, he\'d like to find the one with the lexicographically smallest name.
'''

CREATE PROCEDURE solution()
BEGIN
	SELECT name FROM Products
	ORDER BY price*quantity DESC, name ASC
	LIMIT 1;
END
