import streamlit as st
import plotly.express as px
from user_generator import generate
import pandas as pd

data = generate(count = 50)

df = pd.DataFrame(data)

st.title("Gaphs Pages")

fig = px.pie(df, values = "timezone", names = "first_name")

fig.show()

st.plotly_chart(fig)

st.dataframe(df)