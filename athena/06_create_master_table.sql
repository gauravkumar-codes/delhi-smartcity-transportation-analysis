CREATE TABLE delhi_transport_analysis_db.new_master_dataset
WITH (
    format = 'PARQUET',
    external_location = 's3://dea-delhi-transportation-analysis/curated-zone/master_table/'
) AS

SELECT

    -- Traffic Data (Base)
    t.date,
    t.time,
    t.location,
    t.vehicle_count,
    t.average_speed_kmph,
    t.traffic_density_index,
    t.congestion_level,
    t.road_category,

    -- Accident Data
    a.accident_id,
    a.vehicle_type_at_fault,
    a.victim,
    a.accident_type,
    COALESCE(a.killed, 0) AS killed,
    COALESCE(a.injured, 0) AS injured,
    a.accident_severity,

    -- Weather Data (Daily)
    w.temp_c,
    w.humidity,
    w.precipitation,
    w.windspeed_kph,
    w.condition_text AS weather_condition,

    -- Pollution Data (Daily)
    p.pm2_5,
    p.pm10,
    p.no2,
    p.so2,
    p.co,
    p.aqi

FROM delhi_transport_analysis_db.delhi_traffic t

LEFT JOIN delhi_transport_analysis_db.delhi_accidents a
    ON t.date = a.date
    AND t.time = a.time
    AND t.location = a.location

LEFT JOIN delhi_transport_analysis_db.delhi_weather w
    ON t.date = w.date

LEFT JOIN delhi_transport_analysis_db.delhi_pollution p
    ON t.date = p.date;
