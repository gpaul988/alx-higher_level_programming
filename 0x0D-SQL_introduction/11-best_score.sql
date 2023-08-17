-- Graham S. Paul (11-best_score.sql)
-- Gerating a script that selects score >= 10 in descending order


SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
