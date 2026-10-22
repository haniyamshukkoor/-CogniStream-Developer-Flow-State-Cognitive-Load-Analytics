
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "cognistream_developer_activity_1000_rows.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cognistream_developer_activity_cleaned.csv"
)

REQUIRED_COLUMNS = [
    "event_id",
    "developer_id",
    "team",
    "event_timestamp",
    "activity_type",
    "application",
    "project_name",
    "duration_minutes",
    "interruption_flag",
    "flow_state_proxy",
    "context_switch_flag",
    "data_source",
]


def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)
    original_rows = len(df)

    print("COGNISTREAM DATA CLEANING")
    print("-" * 35)
    print(f"Original rows: {original_rows}")

    # Verify the expected schema before cleaning.
    missing_columns = [
        col for col in REQUIRED_COLUMNS if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Remove exact duplicate records.
    duplicate_rows = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # Remove duplicate event IDs, keeping the first occurrence.
    duplicate_event_ids = int(df["event_id"].duplicated().sum())
    df = df.drop_duplicates(subset=["event_id"], keep="first").copy()

    # Standardize text fields without changing missing values.
    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:
        df[column] = df[column].map(
            lambda value: value.strip() if isinstance(value, str)
            else value
        )

    # Convert timestamps and numeric fields.
    df["event_timestamp"] = pd.to_datetime(
        df["event_timestamp"], errors="coerce"
    )

    df["duration_minutes"] = pd.to_numeric(
        df["duration_minutes"], errors="coerce"
    )

    # Remove rows with invalid essential identifiers or timestamps.
    before_required_checks = len(df)

    df = df.dropna(
        subset=["event_id", "developer_id", "event_timestamp"]
    ).copy()

    invalid_required_rows = before_required_checks - len(df)

    # Remove non-positive or invalid durations.
    invalid_duration_rows = int(
        (df["duration_minutes"].isna()
         | (df["duration_minutes"] <= 0)).sum()
    )

    df = df[
        df["duration_minutes"].notna()
        & (df["duration_minutes"] > 0)
    ].copy()

    # Preserve remaining missing values rather than inventing data.
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Exact duplicate rows removed: {duplicate_rows}")
    print(f"Duplicate event IDs removed: {duplicate_event_ids}")
    print(f"Rows removed for missing required fields: {invalid_required_rows}")
    print(f"Rows removed for invalid duration: {invalid_duration_rows}")
    print(f"Cleaned rows: {len(df)}")
    print(f"Rows removed in total: {original_rows - len(df)}")
    print(f"Remaining missing values: {int(df.isna().sum().sum())}")
    print(f"Cleaned dataset saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
