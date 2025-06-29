-- Shows all TV shows in the hbtn_0d_tvshows database that don’t have any genre linked.
-- Results are sorted by the show title and genre ID in ascending order.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
       WHERE g.`genre_id` IS NULL
 ORDER BY s.`title`, g.`genre_id`;
