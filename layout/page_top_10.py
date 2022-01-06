from dash import dcc
import dash_bootstrap_components as dbc

from .components.viz.top_10_album_score import TOP_10_ALBUM_SCORE_FIG


TOP_10_PAGE = [
    dcc.Graph(figure=TOP_10_ALBUM_SCORE_FIG),
    dcc.Graph(figure=TOP_10_ALBUM_SCORE_FIG),
]
