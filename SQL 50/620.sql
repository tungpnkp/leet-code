select * from Cinema where MOD(id, 2) <> 0 and description not like 'boring'
order by rating desc