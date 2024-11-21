# Objective: Simulate a simplified ETL (Extract, Transform, Load) process.
# Concepts Covered: Data transformation, JSON, list comprehensions, error handling.
# Tasks:
# Read JSON files representing user data (name, age, purchase history).
# Filter users based on certain criteria (e.g., age).
# Transform and store the data in a different format, such as a cleaned-up JSON or CSV.

import pandas as pd
import logging
import os
from datetime import datetime

# Configure Logging
logging.basicConfig(
    filename="etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Set up directory paths (modify as needed)
INPUT_FILE = "inputs/MOCK_DATA.json"
OUTPUT_FILE = "output/transformed_data.csv"
BACKUP_DIR = "backups/"

#Step 1: Extract
def extract_data(file_path):
    
    try:
        # Ensure the file exists
        if not os.path.exists(file_path):
            logging.error(f"Input file not found: {file_path}")
            raise FileNotFoundError(f"File {file_path} does not exist.")
        
        # Read the file into a DataFrame
        data = pd.read_json(file_path, encoding="ISO-8859-1")
        logging.info("Data extraction succesful.")
        return data
    except Exception as e:
        logging.error(f"Error during extraction : {str(e)}")
        raise

# Step2 : Transform
def transform_data(data):
    try:
        #Filtering column to work with
        cols_to_keep = ["name","age","purchase_history","price","quantity", "order_date"]
        data = data[cols_to_keep]

        # Convert ORDERDATE to datetime format
        data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")

        # Add a calculated column: Total Revenue per row
        data["TOTAL_REVENUE"] = data["price"] * data["quantity"]

        logging.info("Data transformation successful.")
        return data

    except Exception as e:
        logging.error(f"Error duing transition : {str(e)}")
        raise

# Step3 : Load
def load_data(data,output_path):
    "Load transformed data to the target location."
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data.to_csv(output_path, index=False)
        logging.info(f"Data succesfully loaded to {output_path}")
    except Exception as e:
        logging.error(f"Error during loading: {str(e)}")
        raise

# Backup Function
def backup_file(file_path, backup_dir):
    """Backup the input file before processing."""
    try:
        os.makedirs(backup_dir, exist_ok=True)
        backup_file_path = os.path.join(
            backup_dir, f"{os.path.basename(file_path)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        os.rename(file_path, backup_file_path)
        logging.info(f"Backup created: {backup_file_path}")
    except Exception as e:
        logging.error(f"Error during backup: {str(e)}")
        raise


# Main ETL Workflow
def etl_pipeline():
    """Run the ETL pipeline."""
    try:
        logging.info("ETL pipeline started.")

        # Step 1: Extract
        data = extract_data(INPUT_FILE)

        # Backup the original file
        backup_file(INPUT_FILE, BACKUP_DIR)

        # Step 2: Transform
        transformed_data = transform_data(data)

        # Step 3: Load
        load_data(transformed_data, OUTPUT_FILE)

        logging.info("ETL pipeline completed successfully.")

    except Exception as e:
        logging.error(f"ETL pipeline failed: {str(e)}")


# Run the ETL pipeline
if __name__ == "__main__":
    etl_pipeline()