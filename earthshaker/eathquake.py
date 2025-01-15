import requests
import pandas as pd
import folium

# USGS Earthquake API URL (past 7 days, all magnitudes)
API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"


def fetch_earthquake_data():
    """Fetch earthquake data from the USGS API and return a Pandas DataFrame."""
    response = requests.get(API_URL)
    data = response.json()

    # Extract relevant fields
    records = []
    for quake in data["features"]:
        props = quake["properties"]
        coords = quake["geometry"]["coordinates"]
        records.append([
            props["place"],
            props["mag"],
            pd.to_datetime(props["time"], unit="ms"),
            coords[1],  # Latitude
            coords[0],  # Longitude
        ])

    return pd.DataFrame(records, columns=["Location", "Magnitude", "Time", "Latitude", "Longitude"])


def plot_earthquakes(df, filename="earthquake_map.html"):
    """Generate an interactive map of earthquake locations using Folium."""
    m = folium.Map(location=[0, 0], zoom_start=2)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Location']} - Magnitude {row['Magnitude']}",
            tooltip=row["Location"],
        ).add_to(m)

    m.save(filename)
    print(f"\nEarthquake map saved as {filename}")


df = fetch_earthquake_data()
plot_earthquakes(df)