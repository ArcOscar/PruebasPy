import pandas as pd
import streamlit as st

gss_data=pd.read_csv("restaurantes.csv")
print("Data imported")

st.title("Pruebas con Heroku")
st.write(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/ehPUumP02x4?start=414" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

st.header("Restaurantes DB")
st.write("")
st.dataframe(gss_data)