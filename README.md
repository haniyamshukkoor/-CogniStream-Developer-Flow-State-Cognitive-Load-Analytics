# CogniStream — Developer Flow-State & Cognitive Load Analytics

## 1. Project Overview

CogniStream is a data analytics project that explores synthetic developer activity patterns, interruptions, context switching, and a flow-state proxy.

It uses Python, Pandas, MySQL, SQL, and Streamlit to clean, analyze, store, and visualize developer activity data.

**Note:** The dataset is synthetic. The flow-state proxy is an analytical indicator, not a direct measurement of a developer's mental state.

## 2. Tech Stack

- **Python** — data processing and analytics
- **Pandas** — data cleaning and manipulation
- **MySQL** — relational database storage
- **SQL** — analytical queries
- **Streamlit** — interactive dashboard
- **Plotly** — interactive charts
- **Matplotlib and Seaborn** — exploratory data visualizations
- **unittest** — automated data quality tests

## 3. Dataset

- **Records:** 1,000 synthetic developer activity events
- **Developers:** 20
- **Time period:** January–December 2025
- **Storage:** CSV files and MySQL database

The dataset includes activity timestamps, teams, applications, project names, event durations, interruption flags, context-switch flags, and a flow-state proxy.

## 4. Features

- Dataset validation and data quality reporting
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Automated dataset quality tests
- SQL analytics by team, activity type, interruption status, and date
- Interactive dashboard with KPI metrics and charts
- CSV-to-MySQL import script

## 5. Project Structure

```text
CogniStream/
├── app/
│   └── dashboard.py
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── reports/
│   └── charts/
├── sql/
│   └── analytics.sql
├── src/
│   ├── analyze_findings.py
│   ├── clean_dataset.py
│   ├── data_quality_report.py
│   ├── explore_dataset.py
│   ├── import_to_mysql.py
│   └── validate_dataset.py
└── tests/
    └── test_dataset.py

## 6. Limitations

- The dataset is synthetic and may not reflect real-world developer behavior.
- The flow-state proxy is not a clinically or scientifically validated measurement of mental state.
- Observed relationships do not establish causation.
- Results should be interpreted as exploratory analytics rather than evidence of individual developer productivity.

## 7. Future Improvements

- Add date-range filters to the dashboard.
- Expand context-switching and application usage analytics.
- Add downloadable analytical reports.
- Improve automated tests for database imports and SQL outputs.
- Add screenshots of the dashboard.

## 8. Author

Maintained as a developer analytics and data engineering portfolio project.

## 9. Dashboard

CogniStream includes an interactive Streamlit dashboard connected to a MySQL database. It provides:

- **Key Performance Indicators (KPIs):** Total activity events, developers, flow-state proxy rate, and interruption rate.
- **Team Analysis:** Comparison of flow-state proxy rates across teams.
- **Interruption Analysis:** Exploration of the relationship between interruptions and the flow-state proxy.
- **Activity Trends:** Daily event volume over time.
- **Activity Summary:** Event counts, average durations, and flow-state proxy rates by activity type.

The dashboard uses Pandas for data processing and Plotly for interactive visualizations.

**Important limitation:** The dataset is synthetic, and the flow-state proxy is an analytical indicator rather than a direct measurement of a developer’s mental state. Observed relationships do not establish causation.


