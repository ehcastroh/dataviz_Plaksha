#!/usr/bin/env python3

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# create dash object ("start app")
app = dash.Dash(__name__)


# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("bii_data_w_categories.csv")

# create list of features for processing
feat_cols = ['trust', 'resilience', 'diversity', 'belief', 'perfection',
       'collaboration', 'comfort zone', 'innovation zone', 'bii score']

# select feature and data (leave response variable data)
y_data = df[feat_cols[:-1]]
x_data = feat_cols

# remove response variable form feature list
res_cols2 = feat_cols[:-1]

# compute mean and standard div
feat_mean = df[res_cols2].mean()
feat_std = df[res_cols2].std()


# ------------------------------------------------------------------------------
# App layout: DASH -- Components/Plots/Callbacks
app.layout = html.Div([
    # design object
    html.H1("Sample Web Application Dashboards with Dash", style={'text-align': 'center'}),

    # interactive component
    dcc.Dropdown(id="slct_group",
        options=[
        {"label": "Sales", "value": "Sales Group"},
                     {"label": "Marketing", "value": "Marketing Group"},
                     {"label": "Operations", "value": "Operations Group"},
                 value="Sales Group",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bii_chart', figure={})

])

"""
# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig
"""

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)