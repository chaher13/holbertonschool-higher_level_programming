-- Script to list all shows from the hbtn_0d_tvshows database that have at least one genre linked.
-- The JOIN operation combines the tv_shows table with the tv_show_genres table based on the show_id and show_id columns.
-- The SELECT statement retrieves the title from the tv_shows table and the genre_id from the tv_show_genres table.
-- The WHERE clause filters the results to include only records where genre_id is not NULL, indicating a genre is linked.
-- The ORDER BY clause sorts the results in ascending order by tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
