import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from .components.sidebar import SIDEBAR
from .page_home import HOME_PAGE
from .page_top_10 import TOP_10_PAGE
from .page_discover import DISCOVER_PAGE
from .page_compare import COMPARE_PAGE


# APP LAYOUT
layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        dbc.Container(
            fluid=True,
            style={"min-height": "100vh", "height": "100vh"},
            children=[
                dbc.Row(
                    children=[
                        SIDEBAR,
                        html.Div(
                            className="col-md-9",
                            id="page-content",
                        ),
                    ]
                ),
            ],
        ),
    ],
)

# PAGE INDEX
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return HOME_PAGE
    elif pathname == "/home":
        return HOME_PAGE
    elif pathname == "/top_10":
        return TOP_10_PAGE
    elif pathname == "/discover":
        return DISCOVER_PAGE
    elif pathname == "/compare":
        return COMPARE_PAGE
    else:
        return "404"
