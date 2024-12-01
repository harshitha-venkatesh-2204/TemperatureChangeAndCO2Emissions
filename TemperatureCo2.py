import plotly.graph_objects as go
import pandas as pd

# Load the dataset
df = pd.read_csv('Co2andTemperatureDecrease.csv')

# Filter necessary columns
df = df[['Year', 'Country', 'Total.CO2', 'Temp_Change']]

# Get unique countries
countries = df['Country'].unique()

# Create a figure
fig = go.Figure()

# Add traces for the first country (default view)
default_country = countries[0]
filtered_df = df[df['Country'] == default_country]

fig.add_trace(
    go.Scatter(
        x=filtered_df['Year'],
        y=filtered_df['Temp_Change'],
        mode='lines+markers',  # Added markers to lines
        name='Temperature Change (°C)',
        line=dict(color='#90be6d', width=4),  # Increased line thickness
        marker=dict(color='#90be6d', size=6)  # Added marker size
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered_df['Year'],
        y=filtered_df['Total.CO2'],
        mode='lines+markers',  # Added markers to lines
        name='CO₂ Emissions (Gigatons)',
        yaxis="y2",
        line=dict(color='#7b2cbf', width=4),  # Increased line thickness
        marker=dict(color='#7b2cbf', size=6)  # Added marker size
    )
)

# Update layout for dual y-axes
fig.update_layout(
    xaxis=dict(
        title="Year",
        titlefont=dict(color="black", size=14, family="Arial, sans-serif"),
        tickfont=dict(color="black", size=12),
        showgrid=False,  # Remove gridlines
        linecolor="black"  # Axis line color
    ),
    yaxis=dict(
        title="Temperature Change (°C)",
        titlefont=dict(color="black", size=14, family="Arial, sans-serif"),
        tickfont=dict(color="black", size=12),
        showgrid=False,  # Remove gridlines
        linecolor="black"  # Axis line color
    ),
    yaxis2=dict(
        title="CO₂ Emissions (Gigatons)",
        titlefont=dict(color="black", size=14, family="Arial, sans-serif"),
        tickfont=dict(color="black", size=12),
        anchor="x",
        overlaying="y",
        side="right",
        showgrid=False,  # Remove gridlines
        linecolor="black"  # Axis line color
    ),
    legend=dict(
        font=dict(color='black', size=14, family="Arial, sans-serif"),
        x=0.01, y=0.99,
        bgcolor="rgba(255,255,255,0)"  # Transparent background for legend
    ),
    paper_bgcolor="white",  # White background for the entire figure
    plot_bgcolor="white"    # White background for the plot
)

# Add dropdown toggle for countries
dropdown_buttons = [
    {
        "label": country,
        "method": "update",
        "args": [
            {"x": [df[df['Country'] == country]['Year'], df[df['Country'] == country]['Year']],
             "y": [df[df['Country'] == country]['Temp_Change'], df[df['Country'] == country]['Total.CO2']]},
            {"title": f"({country})"}
        ]
    }
    for country in countries
]

fig.update_layout(
    updatemenus=[{
        "buttons": dropdown_buttons,
        "direction": "down",
        "showactive": True,  
        "font": dict(color="black", size=14, family="Arial, sans-serif"),  # Dropdown font size
    }]
)

