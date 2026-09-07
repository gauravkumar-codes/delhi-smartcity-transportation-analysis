# 🚦 Delhi Smart City Transportation Analysis

## 📌 Project Overview

The Delhi Smart City Transportation Analysis project uses Amazon Web Services (AWS) to build a scalable, serverless data lakehouse for analyzing urban transportation and environmental data.

The project integrates multiple datasets, including:

- 🚗 Traffic Data
- 🚨 Accident Data
- 🌤️ Weather Data
- 🌫️ Pollution Data

The objective is to identify traffic congestion patterns, accident hotspots, and relationships between transportation and environmental conditions.

---

## 🎯 Objectives

- Build a scalable serverless data pipeline.
- Automate data cleaning and transformation.
- Integrate multiple transportation and environmental datasets.
- Perform SQL-based analysis using Amazon Athena.
- Create interactive dashboards using Amazon QuickSight.
- Generate insights for smart city planning and traffic management.

---

## 🏗️ System Architecture

The project follows a serverless architecture:

```text
                Raw Datasets
                     │
                     ▼
              Amazon S3
                     │
                     ▼
              AWS Lambda
             (Data Processing)
                     │
                     ▼
              Processed Data
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
☁️ AWS Services Used
Amazon S3

Used for storing datasets in different zones:

raw-zone
processed-zone
curated-zone
athena-results
AWS Lambda

Used for automated data cleaning and transformation whenever new CSV files are uploaded to Amazon S3.

Amazon Athena

Used to perform serverless SQL queries and integrate multiple datasets.

Amazon QuickSight

Used to create interactive dashboards and visualize transportation insights.

📊 Dataset Description

The project uses four datasets:

🌤️ Weather Dataset

Contains:

Temperature
Humidity
Wind Speed
Precipitation
Weather Conditions
🚗 Traffic Dataset

Contains:

Location
Traffic Density
Vehicle Count
Road Type
Average Speed
Congestion Level
🚨 Accident Dataset

Contains:

Accident ID
Location
Accident Severity
Vehicle Type at Fault
Number of Injured People
Accident Information
🌫️ Pollution Dataset

Contains:

PM2.5
PM10
NO2
SO2
CO
Air Quality Index (AQI)
🔄 Data Pipeline
CSV Datasets
     ↓
Amazon S3 (Raw Zone)
     ↓
AWS Lambda
     ↓
Data Cleaning & Transformation
     ↓
Amazon S3 (Processed Zone)
     ↓
Amazon Athena
     ↓
Data Integration & Analysis
     ↓
Curated Dataset
     ↓
Amazon QuickSight Dashboard
📈 Key Insights

Some insights generated from the analysis include:

Traffic congestion is highest during morning and evening peak hours.
Certain locations emerge as major accident hotspots.
Higher vehicle volume is associated with poorer air quality.
Weather conditions influence traffic density, vehicle speed, and accident frequency.
Evening traffic contributes significantly to the overall vehicle volume.
🛠️ Technologies Used
Amazon Web Services (AWS)
Amazon S3
AWS Lambda
Amazon Athena
Amazon QuickSight
Python
Pandas
AWS Wrangler
SQL
📂 Project Report

The complete project documentation is available in:

📄 AWS_ProjectReport.pdf

🚀 Future Scope
Integrate AWS SageMaker for traffic prediction.
Predict traffic congestion before it occurs.
Implement edge computing using AWS IoT Greengrass.
Develop APIs for real-time traffic and weather risk information.
👨‍💻 Author

Gaurav Kumar

⭐ If you found this project interesting, feel free to star the repository!


### Recommended GitHub repository structure

```text
Delhi-Smart-City-Transportation-Analysis/
│
├── README.md
│
└── AWS_ProjectReport.pdf
