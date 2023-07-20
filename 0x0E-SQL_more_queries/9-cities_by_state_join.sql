-- select data from 2 tables
SELECT id, name FROM states
SELECT name from cities
ON states.id = cities.state.id
