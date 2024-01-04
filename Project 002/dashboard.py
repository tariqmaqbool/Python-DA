import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

#Page Configure 
st.set_page_config(page_title="H&Y Fashion Sale - Dashboard",page_icon=":shopping_trolley:",layout="wide")
st.title(":shopping_trolley: H&Y Fusion Shop - (Eid Sale Data) Dashboard: Data Analyst using Python")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

#load Data
df = pd.read_csv("sales_data.csv")
df_col = ['Gender','Age','Marital_Status','State','Occupation','Orders','Amount']

#lefe menu
st.sidebar.header("Filter:")
selected_cities = st.sidebar.selectbox("Select City",df['State'].unique())
filter_data = df[(df['State'] == selected_cities)]


#Main Dashboard
st.table(filter_data[df_col])