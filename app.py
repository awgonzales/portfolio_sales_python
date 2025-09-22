import streamlit as st
from user_generator import generate
import pandas as pd

data = generate(count = 50)

df = pd.DataFrame(data)

st.sidebar.title("User Data")

#sidebar - County
county_choice = st.sidebar.selectbox(
    "Select a county:",
    df["county"].sort_values().unique()
    
)

# Show different county information
if county_choice == df:
    st.dataframe(df)