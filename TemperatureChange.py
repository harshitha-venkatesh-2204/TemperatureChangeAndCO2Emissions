import plotly.express as px
import pandas as pd

# Load your dataset (replace with your file path if needed)
df = pd.read_csv('Co2andTemperatureDecrease.csv')

# Select relevant columns
df = df[['Country', 'Temp_Change']]

# Create the choropleth map
fig = px.choropleth(
    df,
    locations="Country",  # Country column for the map
    locationmode='country names',  # Use country names
    color="Temp_Change",  # Color by Temperature Change
    hover_name="Country",  # Hover label showing the country
    hover_data=["Temp_Change"],  # Show Temperature Change in the hover data
    color_continuous_scale="RdBu_r",  # You can change the color scale
    labels={"Temp_Change": "Temperature Change (°C)"},  # Label for the color scale
)

# Update layout to customize map appearance
fig.update_layout(
    geo=dict(
        showcoastlines=True,
        coastlinecolor="Black",  # Coastline color
        projection_type="natural earth",  # Projection type
    ),
    geo_showland=True,
    geo_landcolor="white",  # Land color
    geo_scope="world",  # Scope of the map (worldwide)
)
