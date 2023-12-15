-- select cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states_id = cities.id ORDER BY cities.id;
