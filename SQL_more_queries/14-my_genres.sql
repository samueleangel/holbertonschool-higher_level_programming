-- Shows all the genres linked to the show "Dexter" from the hbtn_0d_tvshows database.
-- Results are sorted by genre name in ascending order.
SELECT g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = s.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;
