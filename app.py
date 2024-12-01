import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import Co2Emissions
import Co2Sources
import TemperatureChange
import TemperatureCo2
import EmissionByCountry
import EmissionAndTemp

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([

    dbc.Navbar(
        dbc.Container([ 
            dbc.NavbarBrand("Temperature Change and CO2 Emissions", style={'color': 'white'}), 
        ]), 
        color="#3a506b", 
        dark=True, 
    ), 

    # Main content area
    html.Div([

        # Row 1: Temperature & CO2 Over Time
        html.Div([ 
            # Temperature & CO2 Over Time Card
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("Temperature & CO2 Over Time", style={'text-align': 'center'}),
                    dcc.Graph(figure=TemperatureCo2.fig),
                ]),
                style={'width': '100%', 'display': 'inline-block', 'margin-bottom': '20px'}
            ),
        ], style={'display': 'flex', 'justify-content': 'center', 'padding': '10px'}),  # Row 1 layout

        # Row 2: World Map (shown twice)
        html.Div([ 
            # World Map Card 1
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("World Map 1", style={'text-align': 'center'}),
                    dcc.Graph(figure=TemperatureChange.fig, style={'height': '450px'}),
                ]),
                style={'width': '48%', 'display': 'inline-block', 'margin-right': '2%', 'margin-bottom': '20px'}
            ),

            # World Map Card 2
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("World Map 2", style={'text-align': 'center'}),
                    dcc.Graph(figure=EmissionByCountry.fig, style={'height': '450px'}),
                ]),
                style={'width': '48%', 'display': 'inline-block', 'margin-bottom': '20px'}
            ),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'padding': '10px'}),  # Row 2 layout

        # Row 3: CO2 Flow Analysis (Sankey) and CO2 Emissions by Source (Bar Chart)
        html.Div([ 
            # CO2 Flow Analysis (Sankey) Card
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("CO2 Flow Analysis (Sankey)", style={'text-align': 'center'}),
                    dcc.Graph(figure=Co2Emissions.fig, style={'height': '400px'}),
                ]),
                style={'width': '48%', 'display': 'inline-block', 'margin-right': '2%', 'margin-bottom': '20px'}
            ),

            # CO2 Emissions by Source (Bar Chart) Card
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("CO2 Emissions by Source (Bar Chart)", style={'text-align': 'center'}),
                    dcc.Graph(figure=Co2Sources.fig, style={'height': '400px'}),
                ]),
                style={'width': '48%', 'display': 'inline-block', 'margin-bottom': '20px'}
            ),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'padding': '10px'}),  # Row 3 layout

        # Row 4: HeatMap (with increased height)
        html.Div([ 
            # HeatMap Card for the fourth row with increased height
            dbc.Card(
                dbc.CardBody([ 
                    html.H4("HeatMap", style={'text-align': 'center'}),
                    dcc.Graph(figure=EmissionAndTemp.fig, style={'height': '800px'}),  # Increased height
                ]),
                style={'width': '100%', 'display': 'inline-block', 'margin-bottom': '20px', 'justify-content': 'center', 'align-items': 'center'}
            ),
        ], style={'display': 'flex', 'justify-content': 'center', 'padding': '10px'}),  # Row 4 layout

    ], style={'padding': '20px'}),  # Padding for the entire content area

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
