from dash import dcc
import dash_bootstrap_components as dbc

COMPARE_PAGE = [
    dbc.Row(
        children=[
            dbc.Col(md=3, children=[dcc.Graph(id="user-stripplot-fig")]),
            dbc.Col(md=9, children=[dcc.Graph(id="user-rank-fig")]),
        ]
    ),
    dbc.Row(
        className="text-center mx-auto", id="compare-text", style={"width": "@200px"}
    ),
    dbc.Row(
        children=[
            dbc.Col(md=6, children=[dcc.Graph(id="user-score-compare-fig")]),
            dbc.Col(md=6, children=[dcc.Graph(id="user-count-compare-fig")]),
        ]
    ),
]
