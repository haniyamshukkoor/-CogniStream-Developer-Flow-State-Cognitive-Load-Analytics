# -CogniStream-Developer-Flow-State-Cognitive-Load-Analytics

## Project Overview

CogniStream is a data analytics project designed to analyze developer activity patterns, coding sessions, and potential interruptions to understand productivity and workflow efficiency. Unlike traditional productivity metrics such as lines of code written or tasks completed, this project focuses on identifying uninterrupted work periods, activity gaps, and context-switching patterns.

Using real-world IDE activity log data, CogniStream transforms raw activity records into meaningful insights through data cleaning, database management, and interactive dashboard visualization.

## Objectives

- Analyze developer activity logs and coding patterns.
- Identify uninterrupted activity sessions and estimate session durations.
- Analyze inactivity gaps and potential context-switching patterns.
- Clean, transform, and organize data for analysis.
- Store and manage structured datasets efficiently.
- Create interactive dashboards to visualize developer activity and productivity trends.

## Technology Stack

- **Python:** Data cleaning, preprocessing, and exploratory data analysis.
- **Microsoft Excel:** Data inspection, basic analysis, and preliminary reporting.
- **MySQL:** Structured data storage, querying, and analytical SQL operations.
- **Power BI:** Interactive dashboards, KPI tracking, and data visualization.

## Key Features

- Developer activity analysis based on timestamped IDE logs.
- Coding session and activity-gap analysis.
- Daily and session-level activity summaries.
- KPI reporting and interactive visualizations.
- Data-driven insights into developer work patterns.

## Project Workflow

1. **Data Collection:** Obtain real-world IDE activity logs from a programming research dataset.
2. **Data Cleaning:** Use Python and Excel to inspect, clean, and prepare the data.
3. **Data Storage:** Load structured data into MySQL for efficient querying and management.
4. **Data Analysis:** Use Python and SQL to calculate session durations, activity gaps, and developer activity metrics.
5. **Dashboard Development:** Connect Power BI to the processed data to build interactive reports and visualizations.

## Expected Outcomes

CogniStream aims to provide a clear understanding of developer activity patterns through measurable indicators such as active session duration, session frequency, inactivity gaps, and daily activity trends.

The project demonstrates an end-to-end data analytics workflow, combining Python-based data processing, Excel, MySQL database management, and Power BI dashboard development.

## Project Scope and Limitations

The initial version focuses on IDE activity logs. Integrating GitHub, Slack, and other development tools may be considered in future enhancements.

Inactivity gaps are indicators of activity patterns and do not necessarily represent interruptions. Cognitive load and mental focus cannot be measured directly from IDE logs alone.

## Conclusion

CogniStream demonstrates how data analytics tools can transform raw developer activity logs into actionable workflow insights. By combining Python, Excel, MySQL, and Power BI, the project aims to support a data-driven understanding of coding sessions and developer activity patterns.
