-- Script to list all genres from the hbtn_0d_tvshows database and display the number of shows linked to each genre.
-- The SELECT statement retrieves the genre from the tv_genres table and counts the number of shows linked to each genre using the COUNT() function.
-- The AS keyword is used to assign aliases to the columns in the result set. The alias "genre" is assigned to the genre column, and the alias "number_of_shows" is assigned to the COUNT() function result.
-- The LEFT JOIN operation combines the tv_genres table with the tv_show_genres table based on the genre_id and genre_id columns.
-- The GROUP BY clause groups the results by genre, so each genre will have a single row in the result set.
-- The HAVING clause filters the results to exclude genres that don't have any shows linked. The COUNT() function result is used to check if the number of shows linked is greater than 0.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING COUNT(tv_show_genres.genre_id) > 0
ORDER BY number_of_shows DESC;
