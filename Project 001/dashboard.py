import streamlit as st
import plotly.express as px

# Heading
st.title("Data Science with Python using (Gap Minder Data) - Data Visualizer")

# Load gapminder data
df = px.data.gapminder()

df_col = ["country", "continent", "year", "lifeExp", "pop", "gdpPercap"]

#Left filter area
st.sidebar.title("Choose your filter:")
selected_year = st.sidebar.slider("Select Year",min_value=1952, max_value=2007)
selected_continent = st.sidebar.selectbox("Select Continent",df['continent'].unique())
selected_pop = st.sidebar.slider("Select Population",min_value=int(df['pop'].min()), max_value=int(df['pop'].max()),value=(int(df['pop'].min()), int(df['pop'].max())))
filter_df = df[(df['year'] == selected_year) &
               (df['continent'] == selected_continent) &
               (df['pop']>= selected_pop[0]) &
               (df['pop'] <= selected_pop[1])]


# Display graph 
fig = px.scatter(filter_df,x="gdpPercap", y="lifeExp", color="country",size="pop", size_max=60,log_x=True, title=f"Life Expectancy Vs GDP per Capital for {selected_year} ")
st.plotly_chart(fig)

# Display table data
st.write(f"Dispaly Data Year: {selected_year}")
st.table(filter_df[df_col])
