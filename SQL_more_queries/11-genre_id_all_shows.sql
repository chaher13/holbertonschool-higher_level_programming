-- Script to list all shows from the hbtn_0d_tvshows database that have at least one genre linked.
-- The LEFT JOIN operation combines the tv_shows table with the tv_show_genres table based on the show_id and show_id columns.
-- The SELECT statement retrieves the title from the tv_shows table and the genre_id from the tv_show_genres table.
-- The LEFT JOIN ensures that all records from tv_shows are included in the result, even if there are no matching records in tv_show_genres. If there is no matching genre_id, it will be displayed as NULL.
-- The ORDER BY clause sorts the results in ascending order by tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
