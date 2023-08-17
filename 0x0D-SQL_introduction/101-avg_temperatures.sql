-- Graham S. Paul (101-avg_temperatures.sql)
-- Next importing table dump into database, cat [filename] | mysql -hlocalhost -uroot -p [database_name]

SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
