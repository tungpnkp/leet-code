select
query_name,
round(sum(rating / position) / count(*), 2) as quality,
round((COUNT(CASE WHEN rating < 3 THEN query_name END) / count(*) ) * 100 , 2 ) as poor_query_percentage
from Queries
where query_name is not null
group by query_name