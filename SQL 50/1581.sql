# Write your MySQL query statement below
select Visits.customer_id, 
count(*) as count_no_trans
from Visits
left join (select visit_id from Transactions group by visit_id) as t2  on Visits.visit_id = t2.visit_id
where t2.visit_id is null 
group by customer_id