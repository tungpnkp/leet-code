(select
"Low Salary" as category,
ifnull((select
count(*) as accounts_count
from Accounts
where income < 20000 ),0) as accounts_count)
union
(select
"Average Salary" as category,
ifnull((select
count(*) as accounts_count
from Accounts
where income between 20000 and 50000),0) as accounts_count)
union
(select
"High Salary" as category,
ifnull((select
count(*) as accounts_count
from Accounts
where income > 50000),0) as accounts_count)
