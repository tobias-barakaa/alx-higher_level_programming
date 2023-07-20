-- Import the database dump from hbtn_0d_tvshows
SELECT tv_genres.name
FROM tvshows
JOIN show_genres ON tvshows.id = show_genres.show_id
JOIN tv_genres ON show_genres.genre_id = tv_genres.id
WHERE tvshows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
