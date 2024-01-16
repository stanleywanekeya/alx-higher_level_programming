-- finds cities

SELECT cities.name from cities join states ON cities.state_id=states.id WHERE states.name="Texas";
