-- Graham S.Paul (12-no_genre.sql)
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

   SELECT tv_shows.title, tv_show_genres.genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.genre_id IS NULL
 ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
