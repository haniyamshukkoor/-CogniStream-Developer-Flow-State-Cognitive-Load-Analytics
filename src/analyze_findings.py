
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "processed" / "cognistream_developer_activity_cleaned.csv"
OUTPUT_PATH = ROOT / "reports" / "eda_findings.md"

df = pd.read_csv(DATA_PATH)
df["event_timestamp"] = pd.to_datetime(
    df["event_timestamp"], errors="coerce"
)

def top_row(series):
    counts = series.dropna().value_counts()
    if counts.empty:
        return "Not available"
    return f"{counts.index[0]} ({counts.iloc[0]} events)"

def top_duration(column):
    totals = df.groupby(column, dropna=False)["duration_minutes"].sum()
    if totals.empty:
        return "Not available"
    name = totals.idxmax()
    label = "Missing" if pd.isna(name) else str(name)
    return f"{label} ({totals.max():,.1f} minutes)"

def flag_rate(column):
    values = pd.to_numeric(df[column], errors="coerce")
    valid = values.isin([0, 1])
    if not valid.any():
        return "Not available"
    return f"{values[valid].mean() * 100:.1f}%"

valid_dates = df["event_timestamp"].dropna()
flow_counts = df["flow_state_proxy"].value_counts(dropna=False)
flow_text = "\n".join(
    f"- `{value}`: {count} events"
    for value, count in flow_counts.items()
)

lines = [
    "# CogniStream — Exploratory Data Analysis Findings",
    "",
    "## 1. Objective",
    "",
    "Explore synthetic developer activity records, recorded time allocation,",
    "interruptions, context switching, and the flow-state proxy.",
    "",
    "## 2. Dataset overview",
    "",
    f"- **Rows analyzed:** {len(df):,}",
    f"- **Unique event IDs:** {df['event_id'].nunique():,}",
    f"- **Unique developers:** {df['developer_id'].nunique():,}",
    f"- **Teams represented:** {df['team'].nunique():,}",
    f"- **Activity types represented:** {df['activity_type'].nunique():,}",
    f"- **Total recorded duration:** {pd.to_numeric(df['duration_minutes'], errors='coerce').sum():,.1f} minutes",
    f"- **Date range:** {valid_dates.min() if not valid_dates.empty else 'Unavailable'} to {valid_dates.max() if not valid_dates.empty else 'Unavailable'}",
    "",
    "## 3. Automatically calculated observations",
    "",
    f"- **Most frequent activity type:** {top_row(df['activity_type'])}.",
    f"- **Most frequent team:** {top_row(df['team'])}.",
    f"- **Activity with the most recorded duration:** {top_duration('activity_type')}.",
    f"- **Project with the most recorded duration:** {top_duration('project_name')}.",
    f"- **Application with the most recorded duration:** {top_duration('application')}.",
    f"- **Interruption-flag rate among valid binary values:** {flag_rate('interruption_flag')}.",
    f"- **Context-switch-flag rate among valid binary values:** {flag_rate('context_switch_flag')}.",
    "",
    "### Flow-state proxy distribution",
    "",
    flow_text,
    "",
    "## 4. Missing values",
    "",
    "| Column | Missing rows |",
    "|---|---:|",
]

for column, count in df.isna().sum().items():
    lines.append(f"| `{column}` | {count:,} |")

lines += [
    "",
    "## 5. Interpretation and limitations",
    "",
    "- This dataset is synthetic; patterns may reflect its generation process.",
    "- Recorded event counts and duration do not directly measure productivity.",
    "- The flow-state proxy is not a direct measurement of mental state or cognitive load.",
    "- Flag rates describe recorded events, not necessarily the percentage of time interrupted.",
    "- Associations between flags and proxy values do not establish causation.",
    "- Review the generated charts before writing additional interpretations.",
    "",
]

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")

print(f"Findings report created: {OUTPUT_PATH}")
print(f"Rows analyzed: {len(df):,}")
print(f"Total recorded duration: "
      f"{pd.to_numeric(df['duration_minutes'], errors='coerce').sum():,.1f} minutes")
print(f"Interruption flag rate: {flag_rate('interruption_flag')}")
print(f"Context-switch flag rate: {flag_rate('context_switch_flag')}")
