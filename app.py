import pandas as pd
import streamlit as st

gss_data=pd.read_csv("restaurantes.csv")
print("Data imported")

st.dataframe(gss_data)