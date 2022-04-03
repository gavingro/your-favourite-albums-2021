from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from data.data import TOTAL_LISTERS, TOTAL_ARTISTS, TOTAL_ALBUMS
from assets.app_colors import APP_COLORS


DISCOVER_PAGE = [
    html.Div(
        className = "px-4 pt-2 my-5",
        children = [
            html.P(
                className="lead mb-3 mt-3 text-center",
                children=[
                    "If we assume that an album's total submission count is representative of it's overall approachability, and that an album's position on each top 10 list is representative of it's overall quality, then we can create 4 ",
                    html.Span("imaginary", id="imaginary-categories", style = {"textDecoration": "underline", "cursor": "pointer"}),
                    " categories for our albums:",
                    dbc.Tooltip(
                        children = [
                            "These assumptions don't hold up under scrutiny.",
                            html.Br(),
                            "Moreover, the boundaries on the graph below are arbitrarily drawn in halfway through the axes, not halfway through the data. Still, the 4 groups give us a fun perspective:",
                            html.Br(),
                            html.Br(),
                            "Hidden Gems (Low Approachability, High Quality)",
                            html.Br(),
                            "Barely Made It (Low Approachability, Low Quality)",
                            html.Br(),
                            "Easy Listening (High Approachability, Low Quality)",
                            html.Br(),
                            "Certified Bangers (High Approachability, High Quality)"
                        ],
                        target="imaginary-categories"
                    )
                ]
            ),
        ]
    ),
    dcc.Graph(
        id="discover-fig",
        config={
            "displayModeBar": False,
        },
    ),
    dbc.Row(
        class_name="text-center mx-auto, pb-4",
        id="discover-text",
    ),
    dbc.Row(
        class_name="pb-4",
        children=dash_table.DataTable(
            id="discover-table",
            style_header={
                "backgroundColor": APP_COLORS["standard"],
                "color": "white",
            },
            page_size=20,
        ),
    ),
]
