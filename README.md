# 🚦 Delhi Smart City Transportation Analysis

## 📌 Project Overview

The **Delhi Smart City Transportation Analysis** project leverages **Amazon Web Services (AWS)** to build a scalable, serverless data lakehouse for analyzing urban transportation and environmental data.

The project integrates multiple datasets, including:

* 🚗 Traffic Data
* 🚨 Accident Data
* 🌤️ Weather Data
* 🌫️ Pollution Data

The objective is to identify traffic congestion patterns, accident hotspots, and relationships between transportation and environmental conditions to support smarter urban planning and traffic management.

---

## 🎯 Objectives

* Build a scalable serverless data pipeline.
* Automate data cleaning and transformation.
* Integrate multiple transportation and environmental datasets.
* Perform SQL-based analysis using Amazon Athena.
* Create interactive dashboards using Amazon QuickSight.
* Generate actionable insights for smart city planning and traffic management.

---

## 🏗️ System Architecture

The project follows a serverless architecture:

```text
                Raw Datasets
                     │
                     ▼
              Amazon S3
                (Raw Zone)
                     │
                     ▼
              AWS Lambda
             (Data Processing)
                     │
                     ▼
              Amazon S3
             (Processed Zone)
                     │
                     ▼
              Amazon Athena
              (SQL Analysis)
                     │
                     ▼
             Curated Dataset
                     │
                     ▼
           Amazon QuickSight
              (Dashboard)
```

---

## ☁️ AWS Services Used

### 🪣 Amazon S3

Used as a data lake to store datasets in different zones:

* `raw-zone`
* `processed-zone`
* `curated-zone`
* `athena-results`

### ⚡ AWS Lambda

Used for automated data cleaning and transformation whenever new CSV files are uploaded to Amazon S3.

### 🔍 Amazon Athena

Used to perform serverless SQL queries, analyze datasets, and integrate multiple data sources.

### 📊 Amazon QuickSight

Used to create interactive dashboards and visualize transportation and environmental insights.

---

## 🗂️ Dataset Description

The project uses four datasets to analyze the relationship between traffic, road accidents, weather conditions, and air pollution in Delhi.

### 🌤️ Weather Dataset (`weather.csv`)

This dataset contains meteorological conditions that may affect traffic patterns, vehicle movement, and road safety.

**Features:**

* Date
* Temperature
* Humidity
* Wind Speed
* Precipitation
* Weather Conditions

---

### 🚗 Traffic Dataset (`traffic.csv`)

This dataset contains information about traffic patterns and congestion across different locations.

**Features:**

* Date
* Location
* Time
* Traffic Density
* Vehicle Count
* Road Type
* Average Speed
* Congestion Level

---

### 🚨 Accident Dataset (`accidents.csv`)

This dataset contains information about road accidents and their severity.

**Features:**

* Accident ID
* Date
* Time
* Location
* Accident Severity
* Vehicle Type at Fault
* Number of Injured People
* Number of Fatalities
* Type of Accident

---

### 🌫️ Pollution Dataset (`pollution.csv`)

This dataset contains air quality measurements used to analyze the environmental impact of transportation.

**Features:**

* Date
* PM2.5
* PM10
* NO₂
* SO₂
* CO
* Air Quality Index (AQI)

---

## 🔗 Data Integration

The datasets are integrated using common attributes such as **Date**, **Location**, and **Time** to analyze relationships between:

* 🚗 Traffic congestion and air pollution
* 🌤️ Weather conditions and traffic patterns
* 🚨 Traffic density and accident frequency
* 🌫️ Vehicle volume and Air Quality Index (AQI)

---

## 🔄 Data Pipeline

```text
CSV Datasets
     │
     ▼
Amazon S3 (Raw Zone)
     │
     ▼
AWS Lambda
     │
     ▼
Data Cleaning & Transformation
     │
     ▼
Amazon S3 (Processed Zone)
     │
     ▼
Amazon Athena
     │
     ▼
Data Integration & Analysis
     │
     ▼
Curated Dataset
     │
     ▼
Amazon QuickSight Dashboard
```

---

## 📈 Key Insights

The analysis generated the following insights:

* 🚗 Traffic congestion is highest during morning and evening peak hours.
* 🚨 Certain locations emerge as major accident hotspots.
* 🌫️ Higher vehicle volume is associated with poorer air quality.
* 🌤️ Weather conditions influence traffic density, vehicle speed, and accident frequency.
* 🌆 Evening traffic contributes significantly to the overall vehicle volume.

---

## 🛠️ Technologies Used

* Amazon Web Services (AWS)
* Amazon S3
* AWS Lambda
* Amazon Athena
* Amazon QuickSight
* Python
* Pandas
* AWS SDK for Pandas (AWS Wrangler)
* SQL

---

## 📂 Project Report

The complete project documentation is available here:

📄 **[Delhi Smart City Transportation Analysis - Project Report](documentation/Delhi_Smart_City_Transportation_Analysis_Report.pdf)**

---

## 📁 Project Structure

```text
Delhi-Smart-City-Transportation-Analysis/
│
├── README.md
│
├── data/
│   ├── accidents.csv
│   ├── pollution.csv
│   ├── traffic.csv
│   └── weather.csv
│
├── lambda/
│   └── lambda_function.py
│
├── athena/
│   ├── create_database.sql
│   ├── create_tables.sql
│   ├── master_dataset.sql
│   └── analysis_queries.sql
│
├── architecture/
│   └── architecture-diagram.png
│
├── dashboards/
│   ├── traffic_density.png
│   ├── accident_analysis.png
│   ├── traffic_vs_aqi.png
│   └── weather_analysis.png
│
├── screenshots/
│   ├── s3/
│   ├── lambda/
│   ├── athena/
│   └── quicksight/
│
└── documentation/
    └── Delhi_Smart_City_Transportation_Analysis_Report.pdf
```

---

## 🚀 Future Scope

* Integrate Amazon SageMaker for traffic prediction.
* Predict traffic congestion before it occurs.
* Implement edge computing using AWS IoT Greengrass.
* Develop APIs for real-time traffic and weather risk information.

---

## 👨‍💻 Author

**Gaurav Kumar**

---

⭐ **If you found this project interesting, feel free to star the repository!**
