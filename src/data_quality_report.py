
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "cognistream_developer_activity_1000_rows.csv"
)
REPORTS_DIR = PROJECT_ROOT / "reports"


def main():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load the original dataset without modifying it
    df = pd.read_csv(DATASET_PATH)

    report_lines = [
        "COGNISTREAM DATA QUALITY REPORT",
        "=" * 40,
        "",
        f"Dataset: {DATASET_PATH.name}",
        f"Number of rows: {len(df)}",
        f"Number of columns: {len(df.columns)}",
        f"Duplicate rows: {df.duplicated().sum()}",
        "",
        "1. MISSING VALUES",
        "-" * 40,
    ]

    missing = df.isnull().sum()

    for column, count in missing.items():
        percentage = (count / len(df) * 100) if len(df) else 0
        report_lines.append(
            f"{column}: {count} missing ({percentage:.2f}%)"
        )

    report_lines.extend([
        "",
        "2. DATA TYPES",
        "-" * 40,
    ])

    for column, dtype in df.dtypes.items():
        report_lines.append(f"{column}: {dtype}")

    report_lines.extend([
        "",
        "3. DUPLICATE EVENT IDs",
        "-" * 40,
    ])

    if "event_id" in df.columns:
        duplicate_ids = df["event_id"].duplicated().sum()
        report_lines.append(
            f"Duplicate event_id values: {duplicate_ids}"
        )
    else:
        report_lines.append("event_id column not found.")

    report_lines.extend([
        "",
        "4. NUMERICAL SUMMARY",
        "-" * 40,
        df.describe(include="number").to_string(),
        "",
        "5. CATEGORICAL SUMMARY",
        "-" * 40,
    ])

    categorical_columns = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns

    for column in categorical_columns:
        report_lines.append(
            f"{column}: {df[column].nunique()} unique values"
        )
        report_lines.append(
            f"  Most common values: "
            f"{df[column].value_counts().head(5).to_dict()}"
        )

    report_lines.extend([
        "",
        "6. END OF REPORT",
        "-" * 40,
        "This report describes the dataset; it does not modify it.",
    ])

    report_path = REPORTS_DIR / "data_quality_report.txt"
    report_path.write_text(
        "\n".join(report_lines) + "\n",
        encoding="utf-8",
    )

    print("\n".join(report_lines))
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
