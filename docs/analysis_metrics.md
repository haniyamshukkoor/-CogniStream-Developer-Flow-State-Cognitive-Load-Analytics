# CogniStream — Analysis Metrics

## 1. Purpose

This document defines the main metrics used to analyze the synthetic
developer activity dataset. Consistent definitions help ensure that
Python analysis, SQL queries, and dashboard calculations use the same
meaning.

## 2. Dataset volume

### Total events
The number of activity records included in an analysis.

Formula: count of event records.

### Unique developers
The number of distinct developer IDs represented in the selected data.

Formula: count of distinct developer IDs.

### Unique teams
The number of distinct team names represented in the selected data.

Formula: count of distinct team names.

## 3. Time allocation

### Total recorded duration
The sum of `duration_minutes` across the selected records.

Formula: sum of `duration_minutes`.

### Average event duration
The mean recorded duration per activity event.

Formula: total recorded duration divided by the number of events.

### Activity duration share
The percentage of all recorded duration associated with an activity type.

Formula: activity duration divided by total duration, multiplied by 100.

Interpretation: this describes recorded time allocation, not productivity.

## 4. Flow-state proxy

### Positive flow-state proxy events
The number of records where `flow_state_proxy` equals 1.

Formula: count of records with `flow_state_proxy = 1`.

### Flow-state proxy rate
The percentage of selected events with a proxy value of 1.

Formula: positive proxy events divided by all selected events,
multiplied by 100.

Interpretation: this is a synthetic indicator, not a direct measurement
of a developer's mental state, cognitive load, or productivity.

## 5. Interruption metrics

### Interrupted event count
The number of records with `interruption_flag = 1`.

### Interruption-flag rate
The percentage of records with a valid interruption flag equal to 1.

Formula: interrupted events divided by records with valid binary flags,
multiplied by 100.

Interpretation: this describes the share of flagged events. It does not
measure the percentage of working time spent interrupted.

## 6. Context-switch metrics

### Context-switch event count
The number of records with `context_switch_flag = 1`.

### Context-switch-flag rate
The percentage of records with a valid context-switch flag equal to 1.

Formula: context-switch events divided by records with valid binary flags,
multiplied by 100.

Interpretation: the rate describes recorded flags and does not establish
whether context switching caused changes in the flow-state proxy.

## 7. Group comparisons

Metrics may be grouped by team, activity type, project, application,
date, or interruption flag.

When comparing groups:
- Report each group's event count alongside its percentage.
- Use the same metric definition across all groups.
- Consider differences in group size and activity mix.
- Avoid causal claims based on descriptive comparisons alone.

## 8. Data and interpretation limitations

- The dataset is synthetic and may reflect its generation rules.
- Results describe the available records, not all real developers.
- Recorded duration is not a direct measure of output or work quality.
- The flow-state proxy is not a validated psychological measurement.
- Associations do not establish causation.
- Small groups may have unstable percentages.
- Confirm the data filters and denominators before comparing results.

## 9. Consistency checklist

Before publishing an analysis:
1. Confirm the dataset and filters being used.
2. Check event counts and unique identifiers.
3. Verify the denominator for every percentage.
4. Confirm that binary flags contain valid values.
5. Compare totals against the source dataset.
6. Label synthetic proxy metrics clearly.
7. Explain limitations alongside conclusions.
