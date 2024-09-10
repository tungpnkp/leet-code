select
round(sum(tiv_2016),2) as tiv_2016
from
Insurance I1
where tiv_2015 in (select tiv_2015 from Insurance I2 where I2.pid != I1.pid group by tiv_2015)
and (lat, lon) not in (select lat, lon from Insurance I3 where I3.pid != I1.pid )