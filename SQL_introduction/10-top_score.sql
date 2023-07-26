-- This script lists all records of the table "second_table" in the "hbtn_0c_0" database on my MySQL server.
-- Results display both the score and the name, ordered by score in descending order (top score first).
SELECT score, name
FROM second_table
ORDER BY score DESC;
