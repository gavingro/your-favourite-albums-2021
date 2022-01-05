import dash_bootstrap_components as dbc
from dash import html

BANNER = dbc.Navbar(
    class_name="navbar navbar-expand-lg navbar-dark bg-dark justify-content-md-between",
    children=[
        dbc.Container(
            fluid=True,
            children=[
                dbc.Col(
                    children=[
                        html.A(
                            className="navbar-brand",
                            href="#",
                            children="Our Favourite Albums",
                        ),
                        dbc.Button(
                            class_name="navbar-toggler",
                            type="button",
                            children=html.Span(className="navbar-toggler-icon"),
                        ),
                    ]
                ),
                dbc.Col(
                    class_name="flex-md-row-reverse",
                    children=[
                        dbc.Collapse(
                            class_name="collapse navbar-collapse",
                            children=[
                                html.Ul(
                                    className="navbar-nav me-auto",
                                    children=[
                                        html.Li(
                                            className="nav-item",
                                            children=[
                                                html.A(
                                                    className="nav-link",
                                                    href="#",
                                                    children=[
                                                        "2021",
                                                        html.Span(
                                                            className="visually-hidden",
                                                            children="(current)",
                                                        ),
                                                    ],
                                                )
                                            ],
                                        )
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
