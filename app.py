import streamlit as st
from user_generator import generate
import pandas as pd

data = generate(count = 50)

st.title("Main Page")