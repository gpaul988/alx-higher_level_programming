-- Graham S. Paul (12-no_cheating.sql)
-- Modernize data in table; change Bob's score to 10

UPDATE second_table SET `score` = 10 WHERE `name` = 'Bob';
