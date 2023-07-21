-- list all the comedy series in a database
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres
on tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
on tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title NOT IN
(SELECT tv_shows.title
	FROM tv_shows
	INNER JOIN tv_show_genres
	on tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres
	on tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title
