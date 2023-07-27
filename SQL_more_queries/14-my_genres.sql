-- Script to list all genres of the TV show 'Dexter' from the hbtn_0d_tvshows database.
-- The SELECT statement retrieves the genre names from the tv_genres table.
-- The JOIN operations are used to combine the tv_genres table with the tv_show_genres table and the tv_shows table based on the genre_id and show_id columns, respectively.
-- The ON keyword specifies the join conditions: tv_genres.id = tv_show_genres.genre_id and tv_show_genres.show_id = tv_shows.id.
-- The WHERE clause filters the results to include only genres related to the TV show 'Dexter'. The condition tv_shows.title = 'Dexter' ensures that only records with the title 'Dexter' in the tv_shows table are included in the result set.
-- The ORDER BY clause sorts the genres in ascending order by name, so the genres appear in alphabetical order.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
