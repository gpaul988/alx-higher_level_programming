-- Graham S. Paul (4-never_empty.sql)
-- Generating table id_not_null
-- Explanation of data in table: id INT with the default value 1, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256)
);
