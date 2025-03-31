--Lowest AQI in Last 3 Months
select 
  min(aqi_us) as lowest_aqi_last_3_months
from {{ source('public', 'weather_air_quality') }}
where ts >= current_date - interval '3 months'

