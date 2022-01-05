import dash_bootstrap_components as dbc
from dash import html

SIDEBAR = [
    dbc.Row(
        justify="center",
        children=[
            dbc.Col(
                children=[
                    dbc.Row(
                        children=[
                            html.A(
                                "Some Placeholder Here", style={"text-align": "center"}
                            )
                        ]
                    ),
                    dbc.Row(
                        children=[
                            html.A(
                                "Some Placeholder Here", style={"text-align": "center"}
                            )
                        ]
                    ),
                    dbc.Row(
                        children=[
                            html.A(
                                "Some Placeholder Here", style={"text-align": "center"}
                            )
                        ]
                    ),
                ],
            )
        ],
    )
]
