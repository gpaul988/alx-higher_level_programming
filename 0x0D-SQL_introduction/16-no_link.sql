-- Graham S. Paul (16-no_link.sql)
-- Giving all details of the table second_table of the database hbtn_0c_0
-- Don’t list rows without a name value

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
