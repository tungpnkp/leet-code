select
sell_date,
count(DISTINCT product) as num_sold,
GROUP_CONCAT( DISTINCT product order by product ASC separator ',' ) as products
from Activities a1
group by sell_date