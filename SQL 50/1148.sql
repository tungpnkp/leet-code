# Write your MySQL query statement below
select distinct v1.author_id as id from Views v1 where v1.author_id = v1.viewer_id order by v1.author_id