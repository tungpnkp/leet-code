select
e1.employee_id,
e1.name,
tmp.reports_count,
tmp.average_age
from Employees e1,
(select e2.reports_to, count(*) as reports_count, round(avg(age), 0) as average_age from Employees e2 where e2.reports_to is not null group by e2.reports_to) as tmp
where tmp.reports_to = e1.employee_id
order by e1.employee_id asc