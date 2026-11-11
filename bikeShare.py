import pandas as pd
import streamlit as st

#reading the .csv file into a dataframe

df = pd.read_csv("./Synthetic Bike Share Data.csv", parse_dates=["start_time"])


#Terminal Output

#five busiest start stations
print("1. Five Busiest Stations Are:")
print(df["start_station"].value_counts().head(5))

#most popular routes
print("-----------------------------------------")
df["route"] = df["start_station"] + " to " + df["end_station"]
print("2. Top 5 Most Popular Routes Are:")
print(df["route"].value_counts().head(5))

#avg trip duration by start station station
print("-----------------------------------------")
print("3.1 Average Duration By Start Station:")
print(df.groupby("start_station")["duration_minutes"].mean().round(1))

#avg trip duration by route
print("-----------------------------------------")
print("3.2 Average Duration By Route:")
print(df.groupby("route")["duration_minutes"].mean().round(1).sort_values(ascending=False).head(10))

#peak travel hours
print("-----------------------------------------")
df["hour"] = df["start_time"].dt.hour
print("4. Peak travel hours")
print(df["hour"].value_counts().head(5))

#streamlit dashboard output

st.title("Bike Share Dashboard")

#adding modified date for the dropdowns
df["date"]  = df["start_time"].dt.date.astype(str)

#dashboard dropdown menus
bike = st.sidebar.selectbox("Bike type", ["All"] + sorted(df["bike_type"].unique()))
day = st.sidebar.selectbox("Day", ["All"] + sorted(df["date"].unique()))
station = st.sidebar.selectbox("Start station", ["All"] + sorted(df["start_station"].unique()))
labels = {"start_station": "Start Station", "route": "Route"}   # raw name -> display name
duration_by = st.sidebar.selectbox("Average Duration By", ["start_station", "route"],
                                   format_func=lambda name: labels[name])

#data filtering based on the dashboard filters
if bike != "All":
    df = df[df["bike_type"] == bike]
if day != "All":
    df = df[df["date"] == day]
if station != "All":
    df = df[df["start_station"] == station]
 
if df.empty:
    st.warning("No trips match these filters.")
    st.stop()
 
st.metric("Trips shown", len(df))

#pandas charts for the processed data
left, right = st.columns(2)
 
left.subheader("Five busiest start stations")
left.bar_chart(df["start_station"].value_counts().head(5), sort=False)
 
right.subheader("Most popular routes")
right.bar_chart(df["route"].value_counts().head(10), sort=False)
 
left.subheader(f"Average duration (min) by {labels[duration_by]}")
avg = df.groupby(duration_by)["duration_minutes"].mean().round(1).sort_values(ascending=False)
left.bar_chart(avg.head(10), sort=False)
 
right.subheader("Trips by hour of day")
right.bar_chart(df["hour"].value_counts().sort_index())
