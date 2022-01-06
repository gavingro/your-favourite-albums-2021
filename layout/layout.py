import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

from .components.banner import BANNER
from .components.sidebar import SIDEBAR
from .components.viz.top_10_album_score import TOP_10_ALBUM_SCORE_FIG


layout1 = html.Div(
    [
        dbc.Container(
            fluid=True,
            children=[
                dbc.Row(
                    children=[
                        SIDEBAR,
                        dbc.Col(
                            class_name="col-md-9",
                            children=[
                                dcc.Graph(figure=TOP_10_ALBUM_SCORE_FIG),
                                dcc.Graph(figure=TOP_10_ALBUM_SCORE_FIG),
                            ],
                        ),
                    ]
                ),
            ],
        ),
    ]
)
