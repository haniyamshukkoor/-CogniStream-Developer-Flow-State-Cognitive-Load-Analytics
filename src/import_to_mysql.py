import pandas as pd
from sqlalchemy import create_engine

CSV_PATH = "data/processed/cognistream_developer_activity_cleaned.csv"

engine = create_engine("mysql+pymysql://cognistream_user:CogniStream_DB_2026%21@localhost/cognistream")

df = pd.read_csv(CSV_PATH)

df.to_sql(
    "activity_events",
    engine,
    if_exists="append",
    index=False,
    chunksize=200,
    method="multi",
)

with engine.connect() as conn:
    total = conn.exec_driver_sql(
        "SELECT COUNT(*) FROM activity_events"
    ).scalar()

print(f"CSV rows: {len(df)}")
print(f"Rows now in MySQL: {total}")
