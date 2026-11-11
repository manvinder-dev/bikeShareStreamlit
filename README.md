# Bike-Share Trip Analysis Dashboard
 
An interactive dashboard that analyses bike-share trip records to understand travel demand. Built with Python, pandas and Streamlit.
 
## What it shows
 
- **Five busiest start stations**: where most trips begin
- **Most popular routes**: the most common start & end station pairs
- **Average trip duration**: by start station or by route
- **Peak travel hours**: number of trips by hour of day
## Dropdown filters
 
Use the sidebar to filter the data:
 
| Dropdown | Options |
|---|---|
| Bike Type | All, classic, electric |
| Day | All, or a specific date |
| Start Station | All, or a specific station |
| Average Duration By | Start Station or Route |
 
## Data
 
`Synthetic Bike Share Data.csv` contains 720 trips from 2026-10-01 to 2026-10-07.
 
| Column | Description |
|---|---|
| `trip_id` | Unique trip identifier |
| `start_time` | Trip start date and time |
| `start_station` | Station where the trip began |
| `end_station` | Station where the trip ended |
| `duration_minutes` | Trip length in minutes |
| `bike_type` | `classic` or `electric` |
 
## Setup
 
1. Install Python 3 and the required packages:
```
   python3 -m pip install pandas streamlit
```
 
2. Keep `bikeShare.py` and the CSV file in the same folder.
## Run
 
From a terminal, in the project folder:
 
```
python3 -m streamlit run bikeShare.py
```
 
The dashboard opens in your browser. Running the file with `python` or from IDLE will not work; it must be launched with `streamlit run`.
