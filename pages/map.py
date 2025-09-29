import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from user_generator import generate

data = generate(count = 50)

df = pd.DataFrame(data)

st.title("Map")

us_locations = folium.Map(location = [40, -95], zoom_start = 4)

# TODO - Add markers for all the data on the map. Use a (For Loop)
folium.Marker(
    location = [40.93121, -73.89875],
    tooltip = "Click Me!",
    popup = "Kelsey Andrade"
).add_to(us_locations)

st_data = st_folium(us_locations)

# st.map(df, color = "#1ef535", zoom = 3)

# st.dataframe(df)
