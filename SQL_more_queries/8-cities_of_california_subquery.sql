-- Script to list all the cities of California found in the database hbtn_0d_usa using a subquery.
-- The subquery retrieves the id of the state where name = California.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
