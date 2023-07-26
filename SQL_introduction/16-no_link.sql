-- This script lists all records with a valid name from the table "second_table".
-- It retrieves all records where the name is not NULL or an empty string.
-- Results display the score and the name, ordered by score in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
