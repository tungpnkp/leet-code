select
Prices.product_id,
(case when sum(units) = 0 or sum(units) is null then 0 else round(sum(units * price) / sum(units) , 2) end)as average_price
from Prices
left join UnitsSold on Prices.product_id = UnitsSold.product_id and purchase_date between start_date and end_date
group by Prices.product_id