import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('Co2andTemperatureDecrease.csv')
energy_sources = ['Coal.Energy', 'Gas.Energy', 'Petroleum.and.other.liquids.Energy', 'Nuclear.Energy', 'Renewables.and.other.Energy']
co2_emissions = ['Coal.CO2', 'Oil.CO2', 'Gas.CO2', 'Cement.CO2', 'Flaring.CO2', 'Other.CO2']
emissions_data = {
    'Coal': df['Coal.CO2'].sum(),
    'Gas': df['Gas.CO2'].sum(),
    'Petroleum': df['Oil.CO2'].sum(),
    'Cement': df['Cement.CO2'].sum(),
    'Flaring': df['Flaring.CO2'].sum(),
    'Other': df['Other.CO2'].sum()
}
traces = []
colors = ['#6b5b95', '#feb236', '#d64161', '#ff7b25', '#92a8d1', '#034f84'] 
for source, color in zip(emissions_data.keys(), colors):
    traces.append(go.Bar(
        x=[source], 
        y=[emissions_data[source]], 
        name=source, 
        marker=dict(color=color) 
    ))
layout = go.Layout(
    xaxis=dict(
        title='Energy',  
        showgrid=False,  
        zeroline=False,
        tickfont=dict(size=9), 
    ),
    yaxis=dict(
        title='Consumption', 
        showgrid=False, 
        zeroline=False, 
        tickfont=dict(size=9), 
    ),
    plot_bgcolor='white', 
    paper_bgcolor='white',
)
fig = go.Figure(data=traces, layout=layout)

