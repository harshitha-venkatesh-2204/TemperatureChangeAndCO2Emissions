import pandas as pd
import plotly.graph_objects as go

file_path = 'Co2andTemperatureDecrease.csv' 
df = pd.read_csv(file_path)

columns_of_interest = ['Year', 'Total.CO2', 'Coal.CO2', 'Oil.CO2', 'Gas.CO2', 'Cement.CO2', 
                       'Flaring.CO2', 'Other.CO2', 'Per.Capita.CO2', 'Total.Energy.Production', 
                       'Coal.Energy', 'Gas.Energy', 'Petroleum.and.other.liquids.Energy', 
                       'Nuclear.Energy', 'Renewables.and.other.Energy', 'CH4', 'Temp_Change']
df = df[columns_of_interest]

df.dropna(inplace=True)

correlation_matrix = df.corr()


fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='RdBu', 
    colorbar=dict(title='Correlation'),
))

fig.update_layout(
    xaxis=dict(
        tickfont=dict(size=10),  
    ),
    yaxis=dict(
        tickfont=dict(size=10), 
    ),
    title_font=dict(size=14), 
    width=1000, 
    height=800,
    margin=dict(l=50, r=50, b=50, t=50),  
)
