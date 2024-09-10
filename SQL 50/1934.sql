# Write your MySQL query statement below
select 
user_id,
(CASE
    WHEN (select count(*) from Confirmations c1 where c1.user_id = s1.user_id) = 0 THEN round(0,2)
    ELSE round((select count(*) from Confirmations c1 where c1.user_id = s1.user_id and c1.action = 'confirmed') / (select count(*) from Confirmations c1 where c1.user_id = s1.user_id ) , 2)
END) as confirmation_rate
from Signups s1