import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import csv

gss_data=pd.read_csv("./restaurantes.csv", delimiter=",")
print("Data imported")

st.dataframe(gss_data)