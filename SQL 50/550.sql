with first_login as (
    select player_id, min(event_date) as first_day from Activity group by player_id
)
select
    round(
        count(fl.player_id)/
        (select count(player_id) from first_login)
    ,2) as fraction
from first_login fl
join Activity a on
    a.player_id = fl.player_id and
    a.event_date = date_add(fl.first_day, INTERVAL 1 DAY)