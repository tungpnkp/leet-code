select
f1.user_id,
count(*) as followers_count
from Followers f1
group by f1.user_id
order by f1.user_id asc