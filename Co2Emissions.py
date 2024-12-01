import pandas as pd
import numpy as np
import plotly.graph_objects as go
from itertools import cycle
from matplotlib.colors import to_rgba, to_hex

file_path = 'Co2andTemperatureDecrease.csv' 
data = pd.read_csv(file_path)
top_countries = data.groupby("Country")["Total.CO2"].sum().nlargest(10).index
filtered_data = data[data["Country"].isin(top_countries)]
emission_sources = ["Coal.CO2", "Oil.CO2", "Gas.CO2", "Cement.CO2", "Flaring.CO2"]
agg_data = filtered_data.groupby("Country")[emission_sources].sum()
agg_data_normalized = agg_data.div(agg_data.sum(axis=1), axis=0)

sources = list(agg_data_normalized.columns)
countries = list(agg_data_normalized.index)
nodes = countries + sources
matrix = agg_data_normalized.T.to_numpy()

colors = cycle(["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880"])
node_colors = [next(colors) for _ in nodes]

def lighten_color(color, amount=0.5):
    """Lightens the given hex color by blending it with white."""
    rgba = to_rgba(color)
    r, g, b, a = rgba
    r = r + (1 - r) * amount
    g = g + (1 - g) * amount
    b = b + (1 - b) * amount
    return to_hex((r, g, b, a)) 

links = []
link_colors = []
for i, source in enumerate(sources):
    for j, country in enumerate(countries):
        value = matrix[i, j]
        if value > 0:
            source_index = len(countries) + i
            target_index = j
            links.append({"source": source_index, "target": target_index, "value": value})
            link_colors.append(lighten_color(node_colors[source_index], amount=0.5))

fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=10,
                thickness=15,
                line=dict(color="black", width=0.5),
                label=nodes,
                color=node_colors,
            ),
            link=dict(
                source=[link["source"] for link in links],
                target=[link["target"] for link in links],
                value=[link["value"] for link in links],
                color=link_colors,
            ),
        )
    ]
)
fig.update_layout(
    font=dict(
        size=10,
        color="black"
    )
)



