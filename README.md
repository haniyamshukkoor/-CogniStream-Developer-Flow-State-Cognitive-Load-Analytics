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


# 🧠 CogniStream
### Developer Flow-State & Cognitive Load Analytics

*Turning developer activity data into meaningful analytical insights.*

---

## 📖 1. Introduction

CogniStream is a data analytics project designed to explore developer activity patterns and study possible indicators associated with focused work, interruptions and context switching.

The project uses a synthetic developer activity dataset and applies Python, SQL, Excel and Power BI to clean, process, analyse and visualize the data.

It also includes an interactive Streamlit dashboard to present analytical findings in an accessible format.

## 🚩 2. Problem Statement

Software developers perform different activities throughout their working day, including coding, debugging, testing, meetings and code reviews.

Frequent interruptions and context switching may affect the continuity of work. However, understanding these activity patterns requires structured data analysis.

CogniStream addresses this analytical problem by examining developer activity records, activity duration, interruptions and context-switch indicators to identify patterns that may be associated with focused work.

## 🎯 3. Aim of the Project

To develop a data analytics solution that explores synthetic developer activity data and visualizes patterns related to activity duration, interruptions, context switching and flow-state proxy indicators.

## 🎯 4. Objectives

- To collect and organize synthetic developer activity data.
- To validate and clean the dataset.
- To perform exploratory data analysis (EDA).
- To analyse activity duration across developers, teams and projects.
- To examine interruption and context-switch patterns.
- To study the distribution of flow-state proxy indicators.
- To perform SQL-based analytical queries.
- To develop an interactive Streamlit dashboard.
- To create Excel reports and visualizations.
- To develop a Power BI dashboard for interactive data exploration.

## 🔍 5. Scope of the Project

The project focuses on descriptive analytics of simulated developer activity.

It covers:

- Developer activity distribution.
- Team-wise and project-wise activity analysis.
- Application usage and time allocation.
- Daily activity patterns.
- Interruption and context-switch rates.
- Flow-state proxy distribution.
- Interactive reporting through Excel, Streamlit and Power BI.

The project is intended for analytical exploration and does not assess the actual mental state or productivity of individual developers.

## 📊 6. Dataset Overview

The project uses a synthetic dataset containing 1,000 developer activity records.

| Dataset Information | Details |
|---|---|
| Total records | 1,000 |
| Developers | 20 |
| Teams | 6 |
| Time period | January–December 2025 |
| Data type | Synthetic |
| File format | CSV |

### Dataset Attributes

| Column | Description |
|---|---|
| event_id | Unique activity event identifier |
| developer_id | Developer identifier |
| team | Team associated with the developer |
| event_timestamp | Date and time of the activity |
| activity_type | Type of developer activity |
| application | Application used |
| project_name | Project associated with the activity |
| duration_minutes | Activity duration in minutes |
| interruption_flag | Indicates whether an interruption is recorded |
| flow_state_proxy | Binary indicator for a possible flow-state event |
| context_switch_flag | Indicates whether a context switch is recorded |
| data_source | Source label of the synthetic event |

## ⚙️ 7. Methodology

The project follows a structured data analytics workflow.

1. **Data Collection:** Obtaining the synthetic developer activity dataset.
2. **Data Validation:** Checking records, columns, missing values and data consistency.
3. **Data Cleaning:** Handling data quality issues and preparing the dataset.
4. **Data Transformation:** Creating useful date and time attributes for analysis.
5. **Exploratory Data Analysis:** Examining distributions, patterns and relationships.
6. **SQL Analytics:** Performing structured queries and aggregations using MySQL.
7. **Data Visualization:** Creating charts and summaries using Python and Plotly.
8. **Dashboard Development:** Building interactive dashboards using Streamlit and Power BI.
9. **Excel Reporting:** Preparing analytical summaries, tables and charts in Excel.

## 📈 8. Data Analysis and Key Findings

The analysis explores activity patterns, duration, team distribution, interruptions and flow-state proxy indicators.

### Overall Project Metrics

| Metric | Result |
|---|---:|
| Total activity events | 1,000 |
| Total developers | 20 |
| Total teams | 6 |
| Total recorded duration | 43,317 minutes |
| Flow-state proxy rate | 31.5% |
| Interruption rate | 12.3% |
| Context-switch rate | 3.5% |

### Activity-wise Analysis

- Coding accounts for 362 events.
- Debugging accounts for 110 events.
- Coding contributes 25,183 minutes, approximately 58.1% of total recorded duration.
- Coding has a flow-state proxy rate of 74.31%.
- Debugging has a flow-state proxy rate of 41.82%.

### Team-wise Analysis

The analysis compares activity records and flow-state proxy rates across six teams.

- Platform has a proxy rate of approximately 32.54%.
- Data has a proxy rate of approximately 32.31%.
- QA has the lowest proxy rate at approximately 27.81%.

### Important Analytical Observation

All 315 events marked with `flow_state_proxy = 1` occur in coding and debugging activities in this synthetic dataset.

These results describe the generated dataset and should not be interpreted as evidence of actual developer mental states or productivity.

## ⚠️ 9. Project Limitations

- The dataset is synthetic and does not represent actual developer behaviour.
- The flow-state proxy is a simulated binary indicator, not a direct measurement of mental state.
- Interruption and context-switch indicators are simulated.
- The analysis identifies descriptive patterns and does not establish causal relationships.
- The results should not be used to evaluate individual developer performance or productivity.

## 🚀 10. Future Enhancements

- Integrate real developer activity data with appropriate consent and privacy safeguards.
- Explore additional analytical techniques for identifying activity patterns.
- Develop more advanced time-series analysis.
- Improve dashboard interactivity and reporting.
- Investigate predictive models using suitable validated data.
- Expand the analysis with additional teams and activity categories.

## ✅ 11. Conclusion

CogniStream demonstrates an end-to-end data analytics workflow using synthetic developer activity data.

The project combines Python-based data processing, exploratory data analysis, MySQL, SQL analytics, Excel reporting, Streamlit visualization and Power BI dashboard development.

It provides an integrated view of developer activity patterns, duration, interruptions and flow-state proxy indicators while highlighting the importance of understanding the limitations of synthetic data.