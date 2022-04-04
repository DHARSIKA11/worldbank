import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.title("World Bank India - Data")
India = pd.read_csv("World_Bank_India.csv",skiprows=4)
st.write(India)
st.write(India.index)
