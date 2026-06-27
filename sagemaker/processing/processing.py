import pandas as pd
from sklearn.model_selection import train_test_split
import boto3
import os

from validation import validate_data
from feature_engineering import feature_engineering

RAW_BUCKET = "salary-mlops-raw-data-445411728398"
PROCESSED_BUCKET = "salary-mlops-processed-data-445411728398"

INPUT_FILE = f"s3://{RAW_BUCKET}/Salary_Data.csv"

print("Reading dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset Shape:", df.shape)

validate_data(df)

df = feature_engineering(df)

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

os.makedirs("processed", exist_ok=True)

train_path = "processed/train.csv"
test_path = "processed/test.csv"

train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)

s3 = boto3.client("s3")

s3.upload_file(
    train_path,
    PROCESSED_BUCKET,
    "train/train.csv"
)

s3.upload_file(
    test_path,
    PROCESSED_BUCKET,
    "test/test.csv"
)

print("\nTrain Shape:", train_df.shape)
print("Test Shape:", test_df.shape)

print("\nFiles uploaded successfully.")
