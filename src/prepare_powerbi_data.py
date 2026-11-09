
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

input_file = ROOT / "data/processed/cognistream_developer_activity_cleaned.csv"
output_file = ROOT / "reports/excel/CogniStream_PowerBI_Data.csv"

df = pd.read_csv(input_file)

df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
df["event_date"] = df["event_timestamp"].dt.date
df["year"] = df["event_timestamp"].dt.year
df["month"] = df["event_timestamp"].dt.month
df["month_name"] = df["event_timestamp"].dt.month_name()
df["weekday"] = df["event_timestamp"].dt.day_name()
df["hour"] = df["event_timestamp"].dt.hour

df.to_csv(output_file, index=False)

print("Power BI dataset created successfully!")
print("Total records:", len(df))
print("Output:", output_file)
