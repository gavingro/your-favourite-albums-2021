from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
import pandas as pd

from data.data import TOTAL_LISTERS, TOTAL_ARTISTS, TOTAL_ALBUMS, AOTY_by_album


DISCOVER_PAGE = [
    dcc.Graph(id="discover-fig"),
    dbc.Row(
        class_name="px-3 pt-4 my-4 text-center",
        children=[
            html.Div(
                className="d-grid gap-2 d-sm-flex justify-content-sm-center",
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                html.H5(
                                    className="card-title", children="Total Voters:"
                                ),
                                html.H6(
                                    className="card-subtitle mb-2 text-muted",
                                    children=TOTAL_LISTERS,
                                ),
                            ]
                        )
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                html.H5(
                                    className="card-title", children="Total Albums:"
                                ),
                                html.H6(
                                    className="card-subtitle mb-2 text-muted",
                                    children=TOTAL_ALBUMS,
                                ),
                            ]
                        )
                    ),
                    dbc.Card(
                        dbc.CardBody(
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
                        )
                    ),
                ],
            ),
        ],
    ),
    # TODO: Add Working Datatable
    # dash_table.DataTable(
    #     id="discover-table",
    # ),
]
