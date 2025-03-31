--Count Readings Per Day This Week
select 
  date_trunc('day', ts) as date,
  count(*) as readings
from {{ source('public', 'weather_air_quality') }}
where date_trunc('week', ts) = date_trunc('week', current_date)
group by 1
order by 1

