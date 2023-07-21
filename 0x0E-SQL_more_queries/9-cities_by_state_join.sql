-- select data from 2 tables
SELECT id, name from cities, name FROM states
ON (states.id = cities.state.id)
ORDER BY cities.id
