-- select data from 2 tables
SELECT id, name FROM cities
SELECT name from states
ON states.id = cities.state.id
