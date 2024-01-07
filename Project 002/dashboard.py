import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

#Page Configure 
st.set_page_config(
    page_title="H&Y Fashion Sale - Dashboard",
    page_icon=":shopping_trolley:",
    layout="wide"
)
st.title(":shopping_trolley: H&Y Fusion Shop - (Eid Sale Data) Dashboard: Data Analyst using Python")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


#load Data
df = pd.read_csv("sales_data.csv", encoding="ISO-8859-1")
df_col = ['Gender','Age','Marital_Status','City','Occupation','Orders','Amount']

#lefe menu
st.sidebar.header("Filter:")
selected_cities = st.sidebar.multiselect("Select City",df['City'].unique())
# occ_list = [''] + list(df['Occupation'].unique())


if not selected_cities:
        filter_data = df
        cities = None
else:
    filter_data = df[df['City'].isin(selected_cities)]
    cities = filter_data["City"].unique()




#Main Dashboard
col1,col2 = st.columns((2))  
#Main Dashboard
with col1:
    st.subheader("Orders by Cities")
    # st.write(f"Dispaly Data Year: {filter_data}")
    city_df = filter_data.groupby(by = ["City"], as_index = False)["Orders"].sum()
    fig = px.bar(city_df, x = "City", y="Orders",template = "seaborn")
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader(f"City wise Sale Report:")
    fig = px.pie(filter_data, values= "Amount", names="City", hole = 0.5)
    fig.update_traces(text = df["City"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)


    # st.subheader(f"Orders by Occupation: {cities}")
    # fig = px.pie(filter_data, values= "Orders", names="Gender", hole = 0.5)
    # fig.update_traces(text = df["Gender"], textposition = "outside")
    # st.plotly_chart(fig,use_container_width=True)
