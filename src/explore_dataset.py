
from pathlib import Path
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "data" / "processed" / "cognistream_developer_activity_cleaned.csv"
CHART_DIR = ROOT / "reports" / "charts"
SUMMARY_FILE = ROOT / "reports" / "eda_summary.txt"

CHART_DIR.mkdir(parents=True, exist_ok=True)


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: reports/charts/{filename}")


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Cleaned dataset not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    df["event_timestamp"] = pd.to_datetime(
        df["event_timestamp"], errors="coerce"
    )

    required = [
        "event_id", "developer_id", "team", "event_timestamp",
        "activity_type", "application", "project_name",
        "duration_minutes", "interruption_flag",
        "flow_state_proxy", "context_switch_flag", "data_source",
    ]
    missing_columns = [c for c in required if c not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    for column in ["duration_minutes", "flow_state_proxy"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["interruption_flag"] = pd.to_numeric(
        df["interruption_flag"], errors="coerce"
    )
    df["context_switch_flag"] = pd.to_numeric(
        df["context_switch_flag"], errors="coerce"
    )

    findings = [
        "COGNISTREAM — EXPLORATORY DATA ANALYSIS",
        "=" * 45,
        f"Rows: {len(df)}",
        f"Columns: {len(df.columns)}",
        f"Unique developers: {df['developer_id'].nunique()}",
        f"Unique teams: {df['team'].nunique()}",
        f"Date range: {df['event_timestamp'].min()} to "
        f"{df['event_timestamp'].max()}",
        "",
        "NUMERICAL SUMMARY",
        df[["duration_minutes", "flow_state_proxy"]].describe().to_string(),
        "",
        "MISSING VALUES",
        df.isna().sum().to_string(),
        "",
        "CHART FINDINGS",
    ]

    def note(text):
        findings.append(text)

    # 1. Activity type counts — univariate
    counts = df["activity_type"].value_counts()
    counts.plot(kind="bar", figsize=(9, 5), title="Events by Activity Type")
    plt.xlabel("Activity type")
    plt.ylabel("Event count")
    plt.xticks(rotation=35, ha="right")
    save_chart("01_activity_type_distribution.png")
    note(f"Most common activity type: {counts.index[0] if len(counts) else 'N/A'}")

    # 2. Events by team — univariate
    counts = df["team"].value_counts()
    counts.plot(kind="bar", figsize=(8, 5), title="Events by Team")
    plt.xlabel("Team")
    plt.ylabel("Event count")
    plt.xticks(rotation=30, ha="right")
    save_chart("02_events_by_team.png")

    # 3. Duration distribution — univariate
    values = df["duration_minutes"].dropna()
    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=20, edgecolor="black")
    plt.title("Activity Duration Distribution")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")
    save_chart("03_duration_distribution.png")
    if len(values):
        note(f"Median activity duration: {values.median():.2f} minutes")

    # 4. Flow-state proxy distribution — univariate
    values = df["flow_state_proxy"].dropna()
    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=15, edgecolor="black")
    plt.title("Flow-State Proxy Distribution")
    plt.xlabel("Flow-state proxy value")
    plt.ylabel("Frequency")
    save_chart("04_flow_proxy_distribution.png")

    # 5. Events over time — temporal
    daily = (
        df.dropna(subset=["event_timestamp"])
        .set_index("event_timestamp")
        .resample("D")["event_id"].count()
    )
    plt.figure(figsize=(10, 5))
    plt.plot(daily.index, daily.values, marker="o")
    plt.title("Recorded Events Over Time")
    plt.xlabel("Date")
    plt.ylabel("Event count")
    plt.xticks(rotation=30)
    save_chart("05_events_over_time.png")

    # 6. Events by application — univariate
    counts = df["application"].value_counts().head(15)
    counts.sort_values().plot(kind="barh", figsize=(8, 5), title="Top Applications by Event Count")
    plt.xlabel("Event count")
    plt.ylabel("Application")
    save_chart("06_events_by_application.png")

    # 7. Events by project — univariate
    counts = df["project_name"].value_counts().head(15)
    counts.sort_values().plot(kind="barh", figsize=(8, 5), title="Top Projects by Event Count")
    plt.xlabel("Event count")
    plt.ylabel("Project")
    save_chart("07_events_by_project.png")

    # 8. Interruption rate by team — bivariate
    temp = df.dropna(subset=["team", "interruption_flag"])
    rates = temp.groupby("team")["interruption_flag"].mean() * 100
    rates.sort_values().plot(kind="bar", figsize=(8, 5), title="Interruption Rate by Team")
    plt.xlabel("Team")
    plt.ylabel("Interrupted events (%)")
    plt.xticks(rotation=30, ha="right")
    save_chart("08_interruption_rate_by_team.png")

    # 9. Context switching rate by activity type — bivariate
    temp = df.dropna(subset=["activity_type", "context_switch_flag"])
    rates = temp.groupby("activity_type")["context_switch_flag"].mean() * 100
    rates.sort_values().plot(kind="bar", figsize=(9, 5), title="Context-Switch Rate by Activity")
    plt.xlabel("Activity type")
    plt.ylabel("Context-switch events (%)")
    plt.xticks(rotation=35, ha="right")
    save_chart("09_context_switch_by_activity.png")

    # 10. Duration vs flow proxy — bivariate
    temp = df.dropna(subset=["duration_minutes", "flow_state_proxy"])
    plt.figure(figsize=(8, 5))
    plt.scatter(temp["duration_minutes"], temp["flow_state_proxy"], alpha=0.5)
    plt.title("Activity Duration vs Flow-State Proxy")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Flow-state proxy")
    save_chart("10_duration_vs_flow_proxy.png")
    if len(temp) >= 2:
        corr = temp["duration_minutes"].corr(temp["flow_state_proxy"])
        note(f"Duration / flow-proxy Pearson correlation: {corr:.3f}")

    # 11. Flow proxy by activity type — bivariate
    temp = df.dropna(subset=["activity_type", "flow_state_proxy"])
    if not temp.empty:
        categories = sorted(temp["activity_type"].unique())
        box_data = [
            temp.loc[temp["activity_type"] == category, "flow_state_proxy"]
            for category in categories
        ]
        plt.figure(figsize=(10, 5))
        plt.boxplot(box_data, tick_labels=categories)
        plt.title("Flow-State Proxy by Activity Type")
        plt.xlabel("Activity type")
        plt.ylabel("Flow-state proxy")
        plt.xticks(rotation=35, ha="right")
        save_chart("11_flow_proxy_by_activity.png")

    # 12. Activity heatmap by weekday and hour — bivariate
    times = df.dropna(subset=["event_timestamp"]).copy()
    times["weekday"] = times["event_timestamp"].dt.dayofweek
    times["hour"] = times["event_timestamp"].dt.hour
    heat = times.pivot_table(
        index="weekday", columns="hour", values="event_id",
        aggfunc="count", fill_value=0
    ).reindex(index=range(7), columns=range(24), fill_value=0)

    plt.figure(figsize=(12, 5))
    plt.imshow(heat, aspect="auto", origin="lower")
    plt.colorbar(label="Event count")
    plt.yticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    plt.xticks(range(24), range(24))
    plt.title("Activity Heatmap by Weekday and Hour")
    plt.xlabel("Hour of day")
    plt.ylabel("Day of week")
    save_chart("12_activity_weekday_hour_heatmap.png")

    # Additional charts to cover identifiers/source and another relationship
    # 13. Events by data source — univariate
    counts = df["data_source"].value_counts()
    counts.plot(kind="bar", figsize=(7, 5), title="Events by Data Source")
    plt.xlabel("Data source")
    plt.ylabel("Event count")
    plt.xticks(rotation=20, ha="right")
    save_chart("13_events_by_data_source.png")

    # 14. Interruption vs flow proxy — bivariate
    temp = df.dropna(subset=["interruption_flag", "flow_state_proxy"])
    if not temp.empty:
        grouped = temp.groupby("interruption_flag")["flow_state_proxy"].mean()
        grouped.plot(kind="bar", figsize=(7, 5), title="Mean Flow Proxy by Interruption Flag")
        plt.xlabel("Interruption flag (0 = no, 1 = yes if encoded that way)")
        plt.ylabel("Mean flow-state proxy")
        plt.xticks(rotation=0)
        save_chart("14_flow_proxy_by_interruption.png")

    # Developer ID and event ID are identifiers; summarize rather than
    # treating them as continuous numeric measurements.
    note(f"Unique event IDs: {df['event_id'].nunique()}")
    note(f"Unique data sources: {df['data_source'].nunique()}")
    note(f"Unique applications: {df['application'].nunique()}")
    note(f"Unique projects: {df['project_name'].nunique()}")

    SUMMARY_FILE.write_text("\n".join(findings) + "\n", encoding="utf-8")
    print("\n".join(findings))
    print(f"\nSummary saved to: {SUMMARY_FILE}")
    print(f"Charts saved in: {CHART_DIR}")


if __name__ == "__main__":
    main()
