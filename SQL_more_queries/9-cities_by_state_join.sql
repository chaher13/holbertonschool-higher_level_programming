-- Script to list all the cities of California found in the database hbtn_0d_usa using a JOIN.
-- The JOIN combines the cities table with the states table based on the state_id and id columns.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
