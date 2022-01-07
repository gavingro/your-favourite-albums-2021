from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


TOP_10_PAGE = [
    dcc.Graph(id="top-10-album-score-fig"),
    html.H6(className="display-6 fw-bold text-center", children="Top 10 Albums"),
    dcc.Graph(id="top-10-album-count-fig"),
]
