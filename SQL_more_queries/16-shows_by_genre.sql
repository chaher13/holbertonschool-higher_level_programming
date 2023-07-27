-- Script to list all TV shows and their linked genres from the hbtn_0d_tvshows database.
-- If a TV show doesn’t have a genre, the genre column will display NULL.
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the TV show title and genre name.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
