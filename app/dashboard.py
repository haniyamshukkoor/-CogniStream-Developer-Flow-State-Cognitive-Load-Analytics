import os
import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine, text

st.set_page_config(page_title="CogniStream", page_icon="📊", layout="wide")
st.title("CogniStream")
st.caption("Developer Activity & Flow-State Proxy Analytics")

@st.cache_resource
def get_engine():
    user = os.getenv("MYSQL_USER", "cognistream_user")
    password = os.getenv("MYSQL_PASSWORD")
    if not password:
        st.error("Set the MYSQL_PASSWORD environment variable first.")
        st.stop()
    return create_engine(
        f"mysql+pymysql://{user}:{password}@localhost/cognistream"
    )

@st.cache_data(ttl=60)
def load_data():
    return pd.read_sql(
        text("SELECT * FROM activity_events"),
        get_engine()
    )

try:
    df = load_data()
except Exception as e:
    st.error(f"Database connection failed: {e}")
    st.stop()

if df.empty:
    st.warning("No activity records found in MySQL.")
    st.stop()

df["event_timestamp"] = pd.to_datetime(df["event_timestamp"], errors="coerce")

st.sidebar.header("Filters")
teams = sorted(df["team"].dropna().unique())
selected_teams = st.sidebar.multiselect("Teams", teams, default=teams)

filtered = df[df["team"].isin(selected_teams)].copy()

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Activity Events", f"{len(filtered):,}")
c2.metric("Developers", filtered["developer_id"].nunique())
c3.metric(
    "Flow Proxy Rate",
    f"{filtered['flow_state_proxy'].mean() * 100:.1f}%"
)
c4.metric(
    "Interruption Rate",
    f"{filtered['interruption_flag'].mean() * 100:.1f}%"
)

left, right = st.columns(2)

with left:
    team_stats = (
        filtered.groupby("team", as_index=False)
        .agg(flow_proxy_rate=("flow_state_proxy", "mean"))
    )
    team_stats["flow_proxy_rate"] *= 100
    st.subheader("Flow-State Proxy by Team")
    st.plotly_chart(
        px.bar(team_stats, x="team", y="flow_proxy_rate",
               labels={"flow_proxy_rate": "Proxy rate (%)", "team": "Team"}),
        use_container_width=True
    )

with right:
    interruption_stats = (
        filtered.groupby("interruption_flag", as_index=False)
        .agg(flow_proxy_rate=("flow_state_proxy", "mean"))
    )
    interruption_stats["flow_proxy_rate"] *= 100
    interruption_stats["Interruption"] = interruption_stats[
        "interruption_flag"
    ].map({0: "No interruption", 1: "Interrupted"})
    st.subheader("Proxy Rate vs. Interruptions")
    st.plotly_chart(
        px.bar(interruption_stats, x="Interruption", y="flow_proxy_rate",
               labels={"flow_proxy_rate": "Proxy rate (%)"}),
        use_container_width=True
    )

st.subheader("Daily Activity Trend")
daily = (
    filtered.dropna(subset=["event_timestamp"])
    .assign(activity_date=lambda x: x["event_timestamp"].dt.date)
    .groupby("activity_date", as_index=False)
    .agg(events=("event_id", "count"),
         flow_proxy_rate=("flow_state_proxy", "mean"))
)
st.plotly_chart(
    px.line(daily, x="activity_date", y="events",
            labels={"activity_date": "Date", "events": "Events"}),
    use_container_width=True
)

st.subheader("Activity Type Summary")
activity = (
    filtered.groupby("activity_type", as_index=False)
    .agg(events=("event_id", "count"),
         avg_duration=("duration_minutes", "mean"),
         flow_proxy_rate=("flow_state_proxy", "mean"))
)
activity["flow_proxy_rate"] *= 100
st.dataframe(activity.round(2), use_container_width=True)

st.caption(
    "Research note: flow_state_proxy is a synthetic proxy, not a direct "
    "measurement of mental state or proof of causation."
)
