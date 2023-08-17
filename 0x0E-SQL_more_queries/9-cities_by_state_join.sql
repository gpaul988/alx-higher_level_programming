-- Graham S. Paul (9-cities_by_state_join.sql)
-- Generating list of the cities in the database hbtn_0d_usa

  SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
   WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
