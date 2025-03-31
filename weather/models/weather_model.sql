SELECT
    DATE(ts) AS date,
    ROUND(AVG(temp)::numeric, 2) AS avg_temp,
    ROUND(MIN(temp)::numeric, 2) AS min_temp,
    ROUND(MAX(temp)::numeric, 2) AS max_temp,
    COUNT(*) AS readings
FROM {{ source('public', 'weather_air_quality') }}
GROUP BY DATE(ts)
ORDER BY date

