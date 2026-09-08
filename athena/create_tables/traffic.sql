CREATE EXTERNAL TABLE IF NOT EXISTS 
delhi_transport_analysis_db.delhi_traffic (

    date STRING,
    time STRING,
    location STRING,
    vehicle_count INT,
    average_speed_kmph DOUBLE,
    traffic_density_index DOUBLE,
    congestion_level STRING,
    road_category STRING

)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','

STORED AS TEXTFILE

LOCATION 's3://dea-delhi-transportation-analysis/processed-zone/traffic/'

TBLPROPERTIES (
    'skip.header.line.count'='1'
);
