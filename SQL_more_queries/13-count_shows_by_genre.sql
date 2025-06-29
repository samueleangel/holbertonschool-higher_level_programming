-- Shows all genres from the hbtn_0d_tvshows database and how many shows are linked to each.
-- It only includes genres that have at least one show.
-- The list is sorted by the number of linked shows, from highest to lowest.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
