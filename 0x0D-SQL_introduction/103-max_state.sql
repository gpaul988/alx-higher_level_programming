-- Graham S. Paul (103-max_state.sql)
-- Shows  maximum temperature of each state

SELECT state, MAX(value) as 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state
