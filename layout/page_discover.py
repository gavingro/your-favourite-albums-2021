from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from data.data import TOTAL_LISTERS, TOTAL_ARTISTS, TOTAL_ALBUMS
from assets.app_colors import APP_COLORS


DISCOVER_PAGE = [
    dbc.Row(
        class_name="pb-1 pt-5 mt-5 text-center",
        children=[
            html.Div(
                className="d-grid gap-5 d-sm-flex justify-content-sm-center",
                children=[
                    dbc.Card(
                        className="shadow",
                        children=dbc.CardBody(
                            children=[
                                html.H5(
                                    className="card-title", children="Total Voters:"
                                ),
                                html.H6(
                                    className="card-subtitle mb-2 text-muted",
                                    children=TOTAL_LISTERS,
                                ),
                            ]
                        ),
                    ),
                    dbc.Card(
                        className="shadow",
                        children=dbc.CardBody(
                            children=[
                                html.H5(
                                    className="card-title", children="Total Albums:"
                                ),
                                html.H6(
                                    className="card-subtitle mb-2 text-muted",
                                    children=TOTAL_ALBUMS,
                                ),
                            ]
                        ),
                    ),
                    dbc.Card(
                        className="shadow",
                        children=dbc.CardBody(
                            children=[
                                html.H5(
                                    className="card-title",
                                    children="Total Artists:",
                                ),
                                html.H6(
                                    className="card-subtitle mb-2 text-muted",
                                    children=TOTAL_ARTISTS,
                                ),
                            ]
                        ),
                    ),
                ],
            ),
        ],
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
    # TODO: Add Working Datatable
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
