from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw/cognistream_developer_activity_1000_rows.csv")

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
    if not DATA_PATH.exists():
        print(f"ERROR: Dataset not found: {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)

    print("=== CogniStream Dataset Validation ===")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        print(f"FAIL: Missing columns: {sorted(missing_columns)}")
        return

    print("PASS: All required columns are present.")

    print(
        "PASS: Expected row count."
        if len(df) == 1000
        else f"WARNING: Expected 1000 rows, found {len(df)}."
    )

    missing_values = df[REQUIRED_COLUMNS].isnull().sum()
    if missing_values.sum() == 0:
        print("PASS: No missing values in required columns.")
    else:
        print("WARNING: Missing values:")
        print(missing_values[missing_values > 0])

    duplicates = df["event_id"].duplicated().sum()
    print(f"Duplicate event IDs: {duplicates}")

    timestamps = pd.to_datetime(df["event_timestamp"], errors="coerce")
    print(f"Invalid timestamps: {timestamps.isna().sum()}")

    durations = pd.to_numeric(df["duration_minutes"], errors="coerce")
    invalid_durations = (durations.isna() | (durations <= 0)).sum()
    print(f"Invalid durations: {invalid_durations}")

    print("\nActivity type counts:")
    print(df["activity_type"].value_counts().to_string())

    print("\nUnique developers:", df["developer_id"].nunique())
    print("\nValidation completed.")


if __name__ == "__main__":
    main()
