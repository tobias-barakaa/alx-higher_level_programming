--  database dump from hbtn_0d_tvshows to your MySQL server: download 
SELECT genre, COUNT(*) AS number_of_shows
FROM tvshows
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;
