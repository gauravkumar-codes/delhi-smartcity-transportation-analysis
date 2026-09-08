CREATE EXTERNAL TABLE IF NOT EXISTS 
delhi_transport_analysis_db.delhi_weather (

    date STRING,
    temp_c DOUBLE,
    humidity DOUBLE,
    precipitation DOUBLE,
    heat_index DOUBLE,
    condition_text STRING

)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','

STORED AS TEXTFILE

LOCATION 's3://dea-delhi-transportation-analysis/processed-zone/weather/'

TBLPROPERTIES (
    'skip.header.line.count'='1'
);
