-- select data from 2 tables
SELECT id, name FROM cities, name FROM states
ON (states.id = cities.state_id)
ORDER BY cities.id ASC;
