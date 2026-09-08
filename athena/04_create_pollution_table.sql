CREATE EXTERNAL TABLE IF NOT EXISTS 
delhi_transport_analysis_db.delhi_pollution (

    date STRING,
    pm2_5 DOUBLE,
    pm10 DOUBLE,
    no2 DOUBLE,
    so2 DOUBLE,
    co DOUBLE,
    aqi DOUBLE

)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','

STORED AS TEXTFILE

LOCATION 's3://dea-delhi-transportation-analysis/processed-zone/pollution/'

TBLPROPERTIES (
    'skip.header.line.count'='1'
);
