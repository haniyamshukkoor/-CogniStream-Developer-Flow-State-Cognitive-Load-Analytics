"""Analyze developer activity patterns in the CogniStream dataset."""

from pathlib import Path

import pandas as pd

INPUT_FILE = Path("data/processed/cognistream_developer_activity_cleaned.csv")
OUTPUT_DIR = Path("reports/analysis")


def load_data(path: Path) -> pd.DataFrame:
    """Load the cleaned dataset and prepare analysis fields."""
    df = pd.read_csv(path)
    df["event_timestamp"] = pd.to_datetime(
        df["event_timestamp"], errors="coerce"
    )
    df["duration_minutes"] = pd.to_numeric(
        df["duration_minutes"], errors="coerce"
    )
    return df


def summarize_group(df: pd.DataFrame, group_column: str) -> pd.DataFrame:
    """Summarize event volume, duration, and proxy rate by group."""
    summary = (
        df.groupby(group_column, dropna=False)
        .agg(
            total_events=("event_id", "count"),
            total_duration_minutes=("duration_minutes", "sum"),
            average_duration_minutes=("duration_minutes", "mean"),
            positive_proxy_events=("flow_state_proxy", "sum"),
            flow_proxy_rate=("flow_state_proxy", "mean"),
            interruption_rate=("interruption_flag", "mean"),
            context_switch_rate=("context_switch_flag", "mean"),
        )
        .reset_index()
    )

    percentage_columns = [
        "flow_proxy_rate",
        "interruption_rate",
        "context_switch_rate",
    ]
    for column in percentage_columns:
        summary[column] = (summary[column] * 100).round(2)

    summary["total_duration_minutes"] = summary[
        "total_duration_minutes"
    ].round(2)
    summary["average_duration_minutes"] = summary[
        "average_duration_minutes"
    ].round(2)

    return summary.sort_values("total_events", ascending=False)


def build_daily_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate daily activity volume, duration, and proxy rate."""
    valid_dates = df.dropna(subset=["event_timestamp"]).copy()
    valid_dates["event_date"] = valid_dates["event_timestamp"].dt.date

    daily = (
        valid_dates.groupby("event_date")
        .agg(
            total_events=("event_id", "count"),
            total_duration_minutes=("duration_minutes", "sum"),
            flow_proxy_rate=("flow_state_proxy", "mean"),
            interruption_rate=("interruption_flag", "mean"),
        )
        .reset_index()
    )

    for column in ["flow_proxy_rate", "interruption_rate"]:
        daily[column] = (daily[column] * 100).round(2)

    return daily


def main() -> None:
    """Run the analysis and export reusable tables."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data(INPUT_FILE)

    if df.empty:
        raise ValueError("The cleaned dataset contains no rows.")

    required_columns = {
        "event_id",
        "event_timestamp",
        "duration_minutes",
        "activity_type",
        "team",
        "flow_state_proxy",
        "interruption_flag",
        "context_switch_flag",
    }
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    analyses = {
        "activity_summary.csv": summarize_group(df, "activity_type"),
        "team_summary.csv": summarize_group(df, "team"),
        "project_summary.csv": summarize_group(df, "project_name"),
        "application_summary.csv": summarize_group(df, "application"),
        "daily_trend.csv": build_daily_trend(df),
    }

    for filename, result in analyses.items():
        result.to_csv(OUTPUT_DIR / filename, index=False)
        print(f"Created {OUTPUT_DIR / filename} ({len(result)} rows)")

    print(f"\nInput events: {len(df)}")
    print(f"Unique developers: {df['developer_id'].nunique()}")
    print(f"Total recorded minutes: {df['duration_minutes'].sum():.2f}")
    print(
        "Overall flow-proxy rate: "
        f"{df['flow_state_proxy'].mean() * 100:.2f}%"
    )
    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
