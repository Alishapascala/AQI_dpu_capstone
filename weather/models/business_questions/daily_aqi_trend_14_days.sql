--Daily AQI Trend Last 14 Days
select 
  date_trunc('day', ts) as date,
  avg(aqi_us) as avg_aqi
from {{ source('public', 'weather_air_quality') }}
where ts >= current_date - interval '14 days'
group by 1
order by 1

