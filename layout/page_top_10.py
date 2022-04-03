from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


TOP_10_PAGE = [
    dcc.Graph(id="top-10-album-score-fig", config={"displayModeBar": False}),
    html.Div(
        className = "text-center",
        children = [
            html.H6(className="display-6 fw-bold", children="Top 10 Albums"),
            html.P(
                className="lead mb-4",
                children=[
                    "As Ranked by ",
                    html.Span(
                        "Album Score",
                        id="top-10-ranked-by",
                    )
                ]
            ),
        ]
    ),
    dcc.Graph(id="top-10-album-count-fig", config={"displayModeBar": False}),
]
