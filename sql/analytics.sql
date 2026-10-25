USE cognistream;

-- 1. Overall dataset summary
SELECT
    COUNT(*) AS total_events,
    COUNT(DISTINCT developer_id) AS total_developers,
    COUNT(DISTINCT team) AS total_teams,
    ROUND(AVG(duration_minutes), 2) AS avg_duration_minutes,
    ROUND(AVG(flow_state_proxy) * 100, 2) AS flow_proxy_rate_pct,
    ROUND(AVG(interruption_flag) * 100, 2) AS interruption_rate_pct,
    ROUND(AVG(context_switch_flag) * 100, 2) AS context_switch_rate_pct
FROM activity_events;

-- 2. Activity by team
SELECT
    team,
    COUNT(*) AS total_events,
    ROUND(AVG(flow_state_proxy) * 100, 2) AS flow_proxy_rate_pct,
    ROUND(AVG(interruption_flag) * 100, 2) AS interruption_rate_pct,
    ROUND(AVG(duration_minutes), 2) AS avg_duration_minutes
FROM activity_events
GROUP BY team
ORDER BY flow_proxy_rate_pct DESC;

-- 3. Activity type analysis
SELECT
    activity_type,
    COUNT(*) AS total_events,
    ROUND(AVG(duration_minutes), 2) AS avg_duration_minutes,
    ROUND(AVG(flow_state_proxy) * 100, 2) AS flow_proxy_rate_pct
FROM activity_events
GROUP BY activity_type
ORDER BY total_events DESC;

-- 4. Interruption comparison
SELECT
    interruption_flag,
    COUNT(*) AS total_events,
    ROUND(AVG(flow_state_proxy) * 100, 2) AS flow_proxy_rate_pct
FROM activity_events
GROUP BY interruption_flag
ORDER BY interruption_flag;

-- 5. Daily trends
SELECT
    DATE(event_timestamp) AS activity_date,
    COUNT(*) AS total_events,
    ROUND(AVG(flow_state_proxy) * 100, 2) AS flow_proxy_rate_pct
FROM activity_events
GROUP BY DATE(event_timestamp)
ORDER BY activity_date;
