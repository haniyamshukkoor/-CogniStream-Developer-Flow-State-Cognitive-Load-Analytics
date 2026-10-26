# CogniStream — Exploratory Data Analysis Findings

## 1. Objective

Explore synthetic developer activity records, recorded time allocation,
interruptions, context switching, and the flow-state proxy.

## 2. Dataset overview

- **Rows analyzed:** 1,000
- **Unique event IDs:** 1,000
- **Unique developers:** 20
- **Teams represented:** 6
- **Activity types represented:** 8
- **Total recorded duration:** 43,317.0 minutes
- **Date range:** 2025-01-01 12:16:57 to 2025-12-31 15:50:34

## 3. Automatically calculated observations

- **Most frequent activity type:** coding (362 events).
- **Most frequent team:** Platform (209 events).
- **Activity with the most recorded duration:** coding (25,183.0 minutes).
- **Project with the most recorded duration:** Analytics Platform (10,324.0 minutes).
- **Application with the most recorded duration:** VS Code (10,826.0 minutes).
- **Interruption-flag rate among valid binary values:** 12.3%.
- **Context-switch-flag rate among valid binary values:** 3.5%.

### Flow-state proxy distribution

- `0`: 685 events
- `1`: 315 events

## 4. Missing values

| Column | Missing rows |
|---|---:|
| `event_id` | 0 |
| `developer_id` | 0 |
| `team` | 0 |
| `event_timestamp` | 0 |
| `activity_type` | 0 |
| `application` | 0 |
| `project_name` | 0 |
| `duration_minutes` | 0 |
| `interruption_flag` | 0 |
| `flow_state_proxy` | 0 |
| `context_switch_flag` | 0 |
| `data_source` | 0 |

## 5. Interpretation and limitations

- This dataset is synthetic; patterns may reflect its generation process.
- Recorded event counts and duration do not directly measure productivity.
- The flow-state proxy is not a direct measurement of mental state or cognitive load.
- Flag rates describe recorded events, not necessarily the percentage of time interrupted.
- Associations between flags and proxy values do not establish causation.
- Review the generated charts before writing additional interpretations.

## 6. Key analytical insights

### Insight 1: Flow-state proxy differs by activity type

Coding had a positive flow-state proxy rate of 74.31% across 362 events. Debugging had a rate of 41.82% across 110 events. The remaining six activity types had no positive proxy events in this dataset.

**Interpretation:** Positive proxy values are concentrated in coding and debugging. This pattern may reflect the synthetic data-generation rules and should not be interpreted as proof that these activities produce flow in real developers.

### Insight 2: Team-level rates are relatively similar

- Platform: 32.54% across 209 events.
- Data: 32.31% across 130 events.
- Frontend: 32.00% across 200 events.
- Backend: 31.94% across 191 events.
- Analytics: 31.93% across 119 events.
- QA: 27.81% across 151 events.

Platform had the highest recorded rate and QA the lowest, a difference of 4.73 percentage points.

**Interpretation:** The recorded rates are relatively close for five teams, while QA is lower. Event counts and activity mix may influence these differences; further investigation is needed before drawing conclusions about teams.

### Insight 3: Coding dominates recorded duration

Coding accounted for 25,183 of 43,317 recorded minutes, approximately 58.1% of total duration.

**Interpretation:** Coding represents the largest share of recorded activity duration. Recorded time alone does not measure productivity or work quality.

## 7. Recommendations and next steps

1. Investigate how the synthetic flow-state proxy was generated, especially why six activity types have no positive values.
2. Compare interruption and non-interruption groups before drawing conclusions about interruptions and the proxy.
3. Examine team activity mix and event counts before interpreting team-level differences.
4. Treat these findings as exploratory patterns in synthetic data, not causal evidence or direct measurements of mental state.

## 8. Analytical reasoning and limitations

The analysis first summarized event counts and durations, then compared the binary flow-state proxy across activity types and teams. Rates were calculated as the proportion of events with a proxy value of 1. Differences were described in percentage points.

The analysis is descriptive. No causal inference or statistical significance testing was performed. The dataset is synthetic, and its patterns may reflect its generation process. Further validation is needed before applying these observations to real developer teams.
