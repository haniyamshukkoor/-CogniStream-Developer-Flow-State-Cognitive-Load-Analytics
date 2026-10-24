
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "processed" / "cognistream_developer_activity_cleaned.csv"
CHART_DIR = ROOT / "reports" / "charts"
SUMMARY_PATH = ROOT / "reports" / "eda_summary.txt"

CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

df["event_timestamp"] = pd.to_datetime(
    df["event_timestamp"], errors="coerce"
)
df = df.dropna(subset=["event_timestamp"]).copy()

df["event_date"] = df["event_timestamp"].dt.date
df["event_hour"] = df["event_timestamp"].dt.hour
df["day_of_week"] = df["event_timestamp"].dt.day_name()
df["day_number"] = df["event_timestamp"].dt.dayofweek

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

def save_chart(filename):
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close()

def bar_chart(data, x, y, title, xlabel, ylabel, filename,
              horizontal=False, rotation=0):
    plt.figure()
    if horizontal:
        sns.barplot(data=data, x=y, y=x)
    else:
        sns.barplot(data=data, x=x, y=y)
        plt.xticks(rotation=rotation, ha="right")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    save_chart(filename)

# 1. Total recorded time by activity type
activity_time = (
    df.groupby("activity_type", dropna=False)["duration_minutes"]
    .sum().reset_index().sort_values("duration_minutes", ascending=False)
)
bar_chart(activity_time, "activity_type", "duration_minutes",
          "Total Recorded Time by Activity Type",
          "Activity Type", "Duration (minutes)",
          "01_time_by_activity.png", horizontal=True)

# 2. Activity distribution by team
team_activity = (
    df.groupby(["team", "activity_type"]).size()
    .reset_index(name="event_count")
)
plt.figure(figsize=(12, 7))
sns.barplot(data=team_activity, y="team", x="event_count",
            hue="activity_type")
plt.title("Recorded Activity Distribution by Team")
plt.xlabel("Number of Events")
plt.ylabel("Team")
plt.legend(title="Activity", bbox_to_anchor=(1.02, 1), loc="upper left")
save_chart("02_activity_by_team.png")

# 3. Duration variability by activity type
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="activity_type", y="duration_minutes")
plt.title("Duration Variability by Activity Type")
plt.xlabel("Activity Type")
plt.ylabel("Duration (minutes)")
plt.xticks(rotation=35, ha="right")
save_chart("03_duration_boxplot.png")

# 4. Flow-state proxy distribution
flow_counts = (
    df["flow_state_proxy"].value_counts(dropna=False)
    .sort_index().rename_axis("flow_state_proxy")
    .reset_index(name="event_count")
)
bar_chart(flow_counts, "flow_state_proxy", "event_count",
          "Flow-State Proxy Distribution",
          "Flow-State Proxy Value", "Number of Events",
          "04_flow_proxy_distribution.png")

# 5. Daily recorded event volume
daily = (
    df.set_index("event_timestamp").resample("D").size()
    .rename("event_count").reset_index()
)
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily, x="event_timestamp", y="event_count")
plt.title("Daily Recorded Event Volume")
plt.xlabel("Date")
plt.ylabel("Number of Events")
save_chart("05_daily_event_volume.png")

# 6. Interruption rate by team
interruption = (
    df.groupby("team")["interruption_flag"].mean()
    .mul(100).rename("interruption_rate_pct")
    .reset_index().sort_values("interruption_rate_pct", ascending=False)
)
bar_chart(interruption, "team", "interruption_rate_pct",
          "Interruption Rate by Team",
          "Team", "Events with Interruption (%)",
          "06_interruption_rate_by_team.png")

# 7. Context-switch rate by activity type
switch_rate = (
    df.groupby("activity_type")["context_switch_flag"].mean()
    .mul(100).rename("context_switch_rate_pct")
    .reset_index().sort_values("context_switch_rate_pct", ascending=False)
)
bar_chart(switch_rate, "activity_type", "context_switch_rate_pct",
          "Context-Switch Rate by Activity Type",
          "Activity Type", "Events with Context Switch (%)",
          "07_context_switch_rate.png", horizontal=True)

# 8. Flow-state proxy by interruption status
plt.figure()
sns.countplot(data=df, x="interruption_flag", hue="flow_state_proxy")
plt.title("Flow-State Proxy by Interruption Status")
plt.xlabel("Interruption Flag (0 = No, 1 = Yes)")
plt.ylabel("Number of Events")
plt.legend(title="Flow-State Proxy")
save_chart("08_flow_by_interruption.png")

# 9. Flow-state proxy by activity type
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="activity_type", y="flow_state_proxy",
            errorbar=None)
plt.title("Mean Flow-State Proxy by Activity Type")
plt.xlabel("Activity Type")
plt.ylabel("Mean Flow-State Proxy")
plt.xticks(rotation=35, ha="right")
save_chart("09_flow_by_activity.png")

# 10. Project time allocation
project_time = (
    df.groupby("project_name", dropna=False)["duration_minutes"]
    .sum().reset_index().sort_values("duration_minutes", ascending=False)
)
bar_chart(project_time, "project_name", "duration_minutes",
          "Recorded Time Allocation by Project",
          "Project", "Duration (minutes)",
          "10_project_time_allocation.png", horizontal=True)

# 11. Application time allocation
app_time = (
    df.groupby("application", dropna=False)["duration_minutes"]
    .sum().reset_index().sort_values("duration_minutes", ascending=False)
)
bar_chart(app_time, "application", "duration_minutes",
          "Recorded Time Allocation by Application",
          "Application", "Duration (minutes)",
          "11_application_time_allocation.png", horizontal=True)

# 12. Day-of-week and hour activity heatmap
heatmap_data = df.pivot_table(
    index="day_number", columns="event_hour",
    values="event_id", aggfunc="count", fill_value=0
).reindex(range(7), fill_value=0)

heatmap_data.index = [
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
]

plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.2)
plt.title("Recorded Event Volume by Day of Week and Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")
save_chart("12_weekday_hour_heatmap.png")

# Summary report
with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
    f.write("COGNISTREAM EXPLORATORY DATA ANALYSIS\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Rows analyzed: {len(df)}\n")
    f.write(f"Unique developers: {df['developer_id'].nunique()}\n")
    f.write(f"Teams: {df['team'].nunique()}\n")
    f.write(
        f"Date range: {df['event_timestamp'].min()} to "
        f"{df['event_timestamp'].max()}\n\n"
    )
    f.write("Events by activity type:\n")
    f.write(df["activity_type"].value_counts(dropna=False).to_string())
    f.write("\n\nEvents by team:\n")
    f.write(df["team"].value_counts(dropna=False).to_string())
    f.write("\n\nTotal recorded duration by activity type (minutes):\n")
    f.write(activity_time.to_string(index=False))
    f.write("\n\nFlow-state proxy distribution:\n")
    f.write(df["flow_state_proxy"].value_counts(dropna=False).to_string())
    f.write("\n\nMissing values by column:\n")
    f.write(df.isna().sum().to_string())
    f.write("\n")

print(f"EDA complete. Charts saved to: {CHART_DIR}")
print(f"Summary saved to: {SUMMARY_PATH}")
print(f"Charts generated: 12")
