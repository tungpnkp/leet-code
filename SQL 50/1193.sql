select
DATE_FORMAT(trans_date, '%Y-%m') as month,
country,
count(*) as trans_count,
count(Case When state = 'approved' then 1 else null end) as approved_count,
sum(amount) as trans_total_amount,
sum(Case When state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by month, country
