import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from .components.banner import BANNER
from .components.sidebar import SIDEBAR
from .components.viz.top_10_album_score import TOP_10_ALBUM_SCORE_FIG


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
                        dbc.Col(
                            className="col-md-9",
                            id="page-content",
                        ),
                    ]
                ),
            ],
        ),
    ],
)

# PAGES

home_page = "HOME"
top_10_page = [
    dcc.Graph(figure=TOP_10_ALBUM_SCORE_FIG),
    dcc.Graph(figure=TOP_10_ALBUM_SCORE_FIG),
]
discover_page = "DISCOVER"
compare_page = "COMPARE"

# PAGE INDEX


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return home_page
    elif pathname == "/home":
        return home_page
    elif pathname == "/top_10":
        return top_10_page
    elif pathname == "/discover":
        return discover_page
    elif pathname == "/compare":
        return compare_page
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
