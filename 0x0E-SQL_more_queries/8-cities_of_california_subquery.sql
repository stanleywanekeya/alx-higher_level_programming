-- subquery for list of cities
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM state_id where name = 'California') ORDER BY id ASC;
