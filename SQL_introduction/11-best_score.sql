-- This script lists all records with a score >= 10 in the table "second_table" in the "hbtn_0c_0" database on your MySQL server.
-- Results display both the score and the name, ordered by score in descending order (top score first).
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
