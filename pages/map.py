import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from user_generator import generate
from user_generator import random_user
# Constants
# TODO: Find proper GEOJSON data for US Regions
MIDWEST_GEOJSON = "https://raw.githubusercontent.com/scdoshi/us-geojson/refs/heads/master/geojson/region/Midwest.geojson"
NORTHEAST_GEOJSON = "https://raw.githubusercontent.com/scdoshi/us-geojson/refs/heads/master/geojson/region/Northeast.geojson"
SOUTH_GEOJSON = "https://raw.githubusercontent.com/scdoshi/us-geojson/refs/heads/master/geojson/region/South.geojson"
WEST_GEOJSON = ""

# Map data
@st.cache_data
def get_data():
    """
    This function will get the data
    """
    data = random_user(count = 100)
    return data
# Dataframe
df = pd.DataFrame(get_data())

#Map
st.title("Map")

st.dataframe(df)

us_locations = folium.Map(location = [40, -95], zoom_start = 4)

#Regions
folium.GeoJson(MIDWEST_GEOJSON,
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5"}).add_to(us_locations)

folium.GeoJson(NORTHEAST_GEOJSON,
    style_function=lambda feature: {
        "fillColor": "#1a993a",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5"}).add_to(us_locations)
folium.GeoJson(SOUTH_GEOJSON,
    style_function=lambda feature: {
        "fillColor": "#e72323",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5"}).add_to(us_locations)

for person in get_data():
    # TODO: Insert HTML PopUP https://python-visualization.github.io/folium/latest/user_guide/ui_elements/popups.html
    latitude = person["latitude"]
    longitude = person["longitude"]
    first_name = person["first_name"]
    last_name = person["last_name"]
    photo = person["photo"]
    html = f"""
            <h5>{first_name} {last_name}</h5><br><img src='{photo}'>
    """
    
    #print(type(latitude), type(longitude))
    folium.Marker(
        location = [latitude, longitude],
        tooltip = "Click Me!",
        popup = html
    ).add_to(us_locations)

st_data = st_folium(us_locations)


# print(data)
# st.map(df, color = "#1ef535", zoom = 3)

# st.dataframe(df)
