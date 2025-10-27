import streamlit as st
from user_generator import random_user
import pandas as pd
import plotly.express as px
import folium 
from streamlit_folium import st_folium

# data = random_user(count = 5)

# Map data
@st.cache_data
def get_data():
    """
    This function will get the data
    """
    data = random_user(count = 100)
    return data

#Dataframe
data = pd.DataFrame(get_data())

# start point
us_locations = folium.Map(location = [40, -95], zoom_start = 4)

fake_data = {
    "Category": ["Yes", "No"],
    "Values": [20,80]
}

# df = pd.DataFrame(get_data())
fake_df = pd.DataFrame(fake_data)

# Page configuration
st.set_page_config(
    page_title = "Sales Dashboard",
    layout = "wide" 
)
 # Chart
st.title("ACME Sales Dashboard")

sales_by_region = px.pie(
    data_frame = fake_data,
    values = "Values",
    names = "Category"
)

st.plotly_chart(sales_by_region)


for person in get_data():
    # TODO: Insert HTML PopUP https://python-visualization.github.io/folium/latest/user_guide/ui_elements/popups.html
    latitude = person["latitude"]
    longitude = person["longitude"]
    location = person["region"]
    sale = person["sales"]
    first_name = person["first_name"]
    last_name = person["last_name"]
    photo = person["photo"]
    html = f"""
            <h5>{first_name} {last_name}</h5><br><img src='{photo}'>
            <h6>'{location}'</h6>
    """

    #print(type(latitude), type(longitude))
    folium.Marker(
        location = [latitude, longitude],
        tooltip = "Click Me!",
        popup = html
    ).add_to(us_locations)

st_data = st_folium(us_locations, width=850)

st.dataframe(data)

st.sidebar.header('Filters')
state = st.sidebar.multiselect(
    label="Select State",
    options = data['state'].unique(),
    default = data['state'].unique()

)

region = st.sidebar.multiselect(
    label = "Select Region",
    options = data['region'].unique(),
    default = data['region'].unique()
)