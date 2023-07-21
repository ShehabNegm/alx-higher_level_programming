-- join 3 tables together
SELECT DISTINCT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
on tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name NOT IN
(SELECT tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres
	on tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	on tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name;
