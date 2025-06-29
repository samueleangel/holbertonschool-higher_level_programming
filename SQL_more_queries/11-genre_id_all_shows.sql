-- Shows all the TV shows in the hbtn_0d_tvshows database.
-- If a show has no genre, it will show NULL.
-- Results are sorted by show title and genre ID in ascending order.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
