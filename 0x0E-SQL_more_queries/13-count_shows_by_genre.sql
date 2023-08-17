-- Graham S. Paul (13-count_shows_by_genre.sql)
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

    SELECT tv_genres.name AS genre, COUNT(*) AS 'number_of_shows'
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY genre
  ORDER BY number_of_shows DESC;
