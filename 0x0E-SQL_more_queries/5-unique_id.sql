-- Graham S. Paul (5-unique_id.sql)
-- Generating table unique_id
-- Explanation of table data: id INT with the default value 1, must be unique & name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
