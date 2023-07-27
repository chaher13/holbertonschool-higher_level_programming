-- Script to list all TV show titles from the hbtn_0d_tvshows database that belong to the genre 'Comedy'.
-- The SELECT statement retrieves the title column from the tv_shows table.
-- The JOIN operations are used to combine the tv_shows table with the tv_show_genres table and the tv_genres table based on the show_id and genre_id columns, respectively.
-- The ON keyword specifies the join conditions: tv_shows.id = tv_show_genres.show_id and tv_show_genres.genre_id = tv_genres.id.
-- The WHERE clause filters the results to include only TV shows that have the genre name 'Comedy'. The condition tv_genres.name = 'Comedy' ensures that only records with the genre name 'Comedy' in the tv_genres table are included in the result set.
-- The ORDER BY clause sorts the TV show titles in ascending order (alphabetical order).
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
-- Script to list all TV show titles from the hbtn_0d_tvshows database that belong to the genre 'Comedy'.
-- The SELECT statement retrieves the title column from the tv_shows table.
-- The JOIN operations are used to combine the tv_shows table with the tv_show_genres table and the tv_genres table based on the show_id and genre_id columns, respectively.
-- The ON keyword specifies the join conditions: tv_shows.id = tv_show_genres.show_id and tv_show_genres.genre_id = tv_genres.id.
-- The WHERE clause filters the results to include only TV shows that have the genre name 'Comedy'. The condition tv_genres.name = 'Comedy' ensures that only records with the genre name 'Comedy' in the tv_genres table are included in the result set.
-- The ORDER BY clause sorts the TV show titles in ascending order (alphabetical order).
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
