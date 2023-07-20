-- select data from 2 tables
SELECT id, name FROM cities, name from states
INNER JOIN cities
ON (states.id = cities.state.id)
ORDER BY cities.id
