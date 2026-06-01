import streamlit as st
import pandas as pd

# Page Title
st.title("Smart Factory Monitoring Dashboard")

# Load Data
df = pd.read_csv("sensordata.csv")

# Show Data
st.subheader("Sensor Data")
st.dataframe(df)

# Latest Values
latest = df.iloc[-1]

st.subheader("Current Machine Status")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature (°C)", latest["Temperature"])
col2.metric("Vibration (mm/s)", latest["Vibration"])
col3.metric("Current (A)", latest["Current"])

# Temperature Chart
st.subheader("Temperature Trend")
st.line_chart(df["Temperature"])

# Vibration Chart
st.subheader("Vibration Trend")
st.line_chart(df["Vibration"])

# Current Chart
st.subheader("Current Trend")
st.line_chart(df["Current"])

# Fault Detection
st.subheader("Machine Health")

if (
    latest["Temperature"] > 80
    or latest["Vibration"] > 7
    or latest["Current"] > 12
):
    st.error("Fault Detected!")
else:
    st.success("Machine Healthy")