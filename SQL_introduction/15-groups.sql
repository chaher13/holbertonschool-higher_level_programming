-- This script retrieves the number of records with the same score from the table "second_table".
-- It uses the SELECT statement with the COUNT() function to calculate the count for each score.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
