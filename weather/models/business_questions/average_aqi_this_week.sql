--Average AQI This Week
select 
  avg(aqi_us) as avg_aqi_this_week
from {{ source('public', 'weather_air_quality') }}
where date_trunc('week', ts) = date_trunc('week', current_date)

