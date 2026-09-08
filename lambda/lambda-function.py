import json
import os
import logging
import urllib.parse

import pandas as pd
import awswrangler as wr


# -------------------------------
# Logging Configuration
# -------------------------------

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    try:
        # ---------------------------------------
        # 1. Extract Bucket and File Information
        # ---------------------------------------

        record = event["Records"][0]

        bucket = record["s3"]["bucket"]["name"]

        key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        logger.info(f"Processing file: s3://{bucket}/{key}")


        # ---------------------------------------
        # 2. Validate File Type
        # ---------------------------------------

        if not key.lower().endswith(".csv"):
            logger.info("File is not a CSV. Skipping processing.")

            return {
                "statusCode": 200,
                "body": json.dumps("Skipped non-CSV file.")
            }


        # ---------------------------------------
        # 3. Prevent Infinite Lambda Trigger Loop
        # ---------------------------------------

        if key.startswith("processed-zone/"):
            logger.info("File already belongs to processed-zone.")

            return {
                "statusCode": 200,
                "body": json.dumps("File already processed.")
            }


        # ---------------------------------------
        # 4. Create Input and Output Paths
        # ---------------------------------------

        input_path = f"s3://{bucket}/{key}"

        output_key = key.replace(
            "raw-zone/",
            "processed-zone/",
            1
        )

        output_path = f"s3://{bucket}/{output_key}"


        # ---------------------------------------
        # 5. Identify Dataset Type
        # ---------------------------------------

        file_name = os.path.basename(key).lower()

        if "traffic" in file_name:
            dataset_type = "traffic"

        elif "accident" in file_name:
            dataset_type = "accident"

        elif "weather" in file_name:
            dataset_type = "weather"

        elif "pollution" in file_name:
            dataset_type = "pollution"

        else:
            logger.warning(
                f"Unknown dataset type: {file_name}"
            )

            return {
                "statusCode": 400,
                "body": json.dumps("Unknown dataset type.")
            }


        logger.info(
            f"Dataset identified as: {dataset_type}"
        )


        # ---------------------------------------
        # 6. Read CSV from S3
        # ---------------------------------------

        df = wr.s3.read_csv(input_path)

        original_rows = len(df)

        logger.info(
            f"Original number of rows: {original_rows}"
        )


        # ---------------------------------------
        # 7. Remove Completely Empty Rows
        # ---------------------------------------

        df.dropna(how="all", inplace=True)


        # ---------------------------------------
        # 8. Dataset-Specific Cleaning
        # ---------------------------------------

        if dataset_type == "traffic":

            numeric_columns = [
                "traffic_density_index",
                "vehicle_count",
                "average_speed_kmph"
            ]


        elif dataset_type == "accident":

            numeric_columns = [
                "injured",
                "killed"
            ]


            # Remove negative values
            if "injured" in df.columns:
                df = df[df["injured"] >= 0]

            if "killed" in df.columns:
                df = df[df["killed"] >= 0]


        elif dataset_type == "weather":

            numeric_columns = [
                "temp_c",
                "humidity",
                "windspeed_kph",
                "precipitation",
                "heat_index"
            ]


        elif dataset_type == "pollution":

            numeric_columns = [
                "pm2_5",
                "pm10",
                "no2",
                "so2",
                "co",
                "aqi"
            ]


        # ---------------------------------------
        # 9. Clean Numeric Columns
        # ---------------------------------------

        for column in numeric_columns:

            if column in df.columns:

                # Convert values to numeric
                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce"
                )

                # Fill missing values using median
                median_value = df[column].median()

                df[column] = df[column].fillna(
                    median_value
                )


        # ---------------------------------------
        # 10. Remove Outliers Using IQR Method
        # ---------------------------------------

        for column in numeric_columns:

            if column in df.columns:

                Q1 = df[column].quantile(0.25)
                Q3 = df[column].quantile(0.75)

                IQR = Q3 - Q1

                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                df = df[
                    (df[column] >= lower_bound)
                    &
                    (df[column] <= upper_bound)
                ]


        # ---------------------------------------
        # 11. Standardize Text Columns
        # ---------------------------------------

        text_columns = df.select_dtypes(
            include=["object"]
        ).columns

        for column in text_columns:

            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )


        # ---------------------------------------
        # 12. Remove Duplicate Rows
        # ---------------------------------------

        df.drop_duplicates(inplace=True)


        # ---------------------------------------
        # 13. Calculate Removed Rows
        # ---------------------------------------

        cleaned_rows = len(df)

        rows_removed = original_rows - cleaned_rows

        logger.info(
            f"Rows removed: {rows_removed}"
        )

        logger.info(
            f"Final number of rows: {cleaned_rows}"
        )


        # ---------------------------------------
        # 14. Write Cleaned Data to Processed Zone
        # ---------------------------------------

        wr.s3.to_csv(
            df=df,
            path=output_path,
            index=False
        )


        logger.info(
            f"Successfully moved cleaned data to: "
            f"{output_path}"
        )


        # ---------------------------------------
        # 15. Return Success Response
        # ---------------------------------------

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File processed successfully",
                "dataset_type": dataset_type,
                "input_path": input_path,
                "output_path": output_path,
                "original_rows": original_rows,
                "final_rows": cleaned_rows,
                "rows_removed": rows_removed
            })
        }


    # ---------------------------------------
    # Error Handling
    # ---------------------------------------

    except Exception as error:

        logger.error(
            f"Error processing file: {str(error)}",
            exc_info=True
        )

        raise error
