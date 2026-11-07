
import pandas as pd
from pathlib import Path

# Project paths
ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data/processed/cognistream_developer_activity_cleaned.csv"
OUTPUT_DIR = ROOT / "reports/excel"
OUTPUT_FILE = OUTPUT_DIR / "CogniStream_Analysis.xlsx"

# Load dataset
df = pd.read_csv(INPUT_FILE)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Convert timestamp
df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
df["date"] = df["event_timestamp"].dt.date
df["weekday"] = df["event_timestamp"].dt.day_name()
df["hour"] = df["event_timestamp"].dt.hour

# Create analysis summaries
activity = df.groupby("activity_type").agg(
    total_events=("event_id", "count"),
    total_duration=("duration_minutes", "sum"),
    average_duration=("duration_minutes", "mean"),
    flow_events=("flow_state_proxy", "sum")
).reset_index()

activity["flow_rate_percent"] = (
    activity["flow_events"] / activity["total_events"] * 100
)

team = df.groupby("team").agg(
    total_events=("event_id", "count"),
    total_duration=("duration_minutes", "sum"),
    flow_events=("flow_state_proxy", "sum")
).reset_index()

team["flow_rate_percent"] = (
    team["flow_events"] / team["total_events"] * 100
)

project = df.groupby("project_name").agg(
    total_events=("event_id", "count"),
    total_duration=("duration_minutes", "sum")
).reset_index()

application = df.groupby("application").agg(
    total_events=("event_id", "count"),
    total_duration=("duration_minutes", "sum")
).reset_index()

daily = df.groupby("date").agg(
    total_events=("event_id", "count"),
    total_duration=("duration_minutes", "sum"),
    flow_events=("flow_state_proxy", "sum")
).reset_index()

# Export Excel workbook
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    activity.to_excel(writer, sheet_name="Activity Analysis", index=False)
    team.to_excel(writer, sheet_name="Team Analysis", index=False)
    project.to_excel(writer, sheet_name="Project Analysis", index=False)
    application.to_excel(writer, sheet_name="Application Analysis", index=False)
    daily.to_excel(writer, sheet_name="Daily Trends", index=False)

print("Excel workbook created successfully!")
print(f"Saved at: {OUTPUT_FILE}")
print(f"Total records: {len(df)}")

from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.chart import BarChart, LineChart, Reference

# Open generated workbook
wb = load_workbook(OUTPUT_FILE)

# Format every worksheet
for ws in wb.worksheets:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(
            start_color="17365D",
            end_color="17365D",
            fill_type="solid"
        )
        cell.alignment = Alignment(horizontal="center")

    for column in ws.columns:
        max_length = max(
            len(str(cell.value or "")) for cell in column
        )
        ws.column_dimensions[column[0].column_letter].width = min(
            max_length + 3, 30
        )

# Add Excel tables to summary sheets
for sheet_name, table_name in [
    ("Activity Analysis", "ActivityTable"),
    ("Team Analysis", "TeamTable"),
    ("Project Analysis", "ProjectTable"),
    ("Application Analysis", "ApplicationTable"),
    ("Daily Trends", "DailyTable")
]:
    ws = wb[sheet_name]
    tab = Table(
        displayName=table_name,
        ref=ws.dimensions
    )
    tab.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2",
        showRowStripes=True
    )
    ws.add_table(tab)

# Activity chart
ws = wb["Activity Analysis"]
chart = BarChart()
chart.title = "Total Duration by Activity"
chart.y_axis.title = "Duration (Minutes)"
chart.x_axis.title = "Activity"

data = Reference(ws, min_col=3, min_row=1, max_row=ws.max_row)
categories = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
ws.add_chart(chart, "H2")

# Team flow proxy chart
ws = wb["Team Analysis"]
chart = BarChart()
chart.title = "Flow-State Proxy Rate by Team"
chart.y_axis.title = "Flow Rate (%)"
chart.x_axis.title = "Team"

data = Reference(ws, min_col=5, min_row=1, max_row=ws.max_row)
categories = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
ws.add_chart(chart, "G2")

# Daily trend chart
ws = wb["Daily Trends"]
chart = LineChart()
chart.title = "Daily Activity Volume"
chart.y_axis.title = "Number of Events"
chart.x_axis.title = "Date"

data = Reference(ws, min_col=2, min_row=1, max_row=ws.max_row)
categories = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
ws.add_chart(chart, "G2")

# Save formatted workbook
wb.save(OUTPUT_FILE)

print("Formatting and charts added successfully!")

