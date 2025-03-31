--Highest AQI This Week
select 
  max(aqi_us) as highest_aqi_this_week
from {{ source('public', 'weather_air_quality') }}
where date_trunc('week', ts) = date_trunc('week', current_date)

