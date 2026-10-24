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
