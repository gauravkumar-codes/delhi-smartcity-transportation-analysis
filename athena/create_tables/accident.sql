CREATE EXTERNAL TABLE IF NOT EXISTS 
delhi_transport_analysis_db.delhi_accidents (

    accident_id STRING,
    date STRING,
    time STRING,
    location STRING,
    vehicle_type_at_fault STRING,
    victim STRING,
    accident_type STRING,
    killed INT,
    injured INT,
    accident_severity STRING

)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','

STORED AS TEXTFILE

LOCATION 's3://dea-delhi-transportation-analysis/processed-zone/accidents/'

TBLPROPERTIES (
    'skip.header.line.count'='1'
);
