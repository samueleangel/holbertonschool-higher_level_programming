-- Displays all shows from the hbtn_0d_tvshows database that are associated with at least one genre.
-- The results are ordered by tv_shows.title (ascending) and then by tv_show_genres.genre_id (ascending).
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
