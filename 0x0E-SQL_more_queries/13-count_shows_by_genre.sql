-- script to count shows by geners
SELECT tv_genres.name AS genre, 
count(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;


