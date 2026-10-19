# CogniStream Dataset Data Dictionary

## 1. Project Overview

CogniStream is a Developer Flow-State and Cognitive Load Analytics
project. It explores developer activity patterns using a simulated
dataset and data analytics tools.

The project uses Python for data processing, MySQL for structured
storage, Excel for preliminary analysis, and Power BI for dashboards.

## 2. Dataset Information

- Dataset file: cognistream_developer_activity_1000_rows.csv
- Expected number of records: 1,000
- Expected number of columns: 12
- Data type: Synthetic, simulated developer activity data
- Intended use: Learning, exploratory analysis, and dashboard development
- Time period represented: January 1 to December 31, 2025
- The dataset does not represent real individual developers.

## 3. Column Definitions

### event_id
Unique identifier assigned to an activity event.
It can be used to identify records and check for duplicate events.

### developer_id
Identifier for a simulated developer.
It supports grouping and comparing activity patterns.

### team
Team assigned to the simulated developer activity.
It can support team-level summaries.

### event_timestamp
Date and time associated with the activity event.
It can support daily, weekly, monthly, and hourly analysis.

### activity_type
Category of activity, such as coding, debugging, code review,
testing, meeting, notification, documentation, or break.
It supports analysis of time spent across activity categories.

### application
Application associated with the recorded activity.
It can help summarize activity by application.

### project_name
Name of the simulated project associated with the event.
It supports project-level comparisons.

### duration_minutes
Duration of the activity, measured in minutes.
It can support total-duration and average-duration calculations.

### interruption_flag
Simulated indicator of whether an event is associated with an
interruption. Its values are intended to be binary.
It does not prove that a person experienced a real interruption.

### flow_state_proxy
Heuristic indicator intended for exploratory analysis of activity
patterns that may be associated with focused work.
It is not a clinical measure or a direct measurement of mental state.

### context_switch_flag
Simulated indicator of a possible context switch.
Its interpretation depends on the dataset's generation rules.
It should not be treated as a verified measure of cognitive load.

### data_source
Indicates the source category represented by the simulated event.
It provides context for grouping records by source.

## 4. Planned Data Quality Checks

The dataset will be checked for:
- Presence of all expected columns
- Expected row count
- Missing values
- Duplicate event identifiers
- Valid event timestamps
- Positive activity durations
- Valid values for binary indicator columns
- Consistent activity categories

These checks are planned; they have not yet been completed.

## 5. Planned Analytical Uses

The dataset may be used to explore:
- Activity duration by type
- Activity patterns over time
- Comparisons between simulated teams
- Distribution of activity across applications
- Interruption and context-switch indicators
- Exploratory flow-state proxy patterns

## 6. Limitations and Responsible Interpretation

This dataset is synthetic and does not describe actual employees.
The flow-state proxy and context-switch indicators are simplified
heuristics rather than validated psychological measurements.

Observed patterns should not be used to diagnose cognitive load,
judge individual performance, or make employment decisions.

Any conclusions from analysis should acknowledge the simulated
nature and limitations of the dataset.

## 7. Planned Project Workflow

1. Document the dataset.
2. Validate the source CSV using Python.
3. Investigate and handle data quality issues.
4. Prepare clean data for analysis.
5. Design and create MySQL tables.
6. Load and query the dataset in MySQL.
7. Explore the data using Excel.
8. Develop Power BI measures and dashboards.
9. Document findings and project limitations.
