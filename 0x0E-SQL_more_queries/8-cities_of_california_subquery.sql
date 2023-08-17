-- Graham S. Paul (8-cities_of_california_subquery.sql)
-- Generating database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- Expalnation of table data

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
