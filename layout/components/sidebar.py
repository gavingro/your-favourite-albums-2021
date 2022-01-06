import dash_bootstrap_components as dbc
from dash import html

SIDEBAR = dbc.Col(
    class_name="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark",
    style={"width": "280px"},
    width=280,
    children=[
        html.A(
            className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none",
            href="/",
            children=[
                html.Img(className="bi me-2", height=44, src="assets/cd_icon.png"),
                html.Span(
                    className="fs-4 fw-bold lh-1", children="Your Favourite Albums 2021"
                ),
            ],
        ),
        html.Hr(),
        dbc.Nav(
            className="nav nav-pills flex-column mb-auto",
            children=[
                dbc.NavItem(
                    children=[
                        dbc.NavLink(
                            active=True,
                            href="#",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=16,
                                    width=16,
                                    src="assets/cd_icon.png",
                                ),
                                html.Span(
                                    className="fs-6 fw-light p-3", children="Top 10"
                                ),
                            ],
                        )
                    ]
                ),
                dbc.NavItem(
                    children=[
                        dbc.NavLink(
                            active="partial",
                            href="#",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=16,
                                    width=16,
                                    src="assets/cd_icon.png",
                                ),
                                html.Span(
                                    className="fs-6 fw-light p-3", children="Discovery"
                                ),
                            ],
                        )
                    ]
                ),
                dbc.NavItem(
                    children=[
                        dbc.NavLink(
                            active="partial",
                            href="#",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=16,
                                    width=16,
                                    src="assets/cd_icon.png",
                                ),
                                html.Span(
                                    className="fs-6 fw-light p-3", children="Compare"
                                ),
                            ],
                        )
                    ]
                ),
            ],
        ),
        html.Hr(),
        html.Span(className="fs-6 fw-light p-2", children="Album Search"),
        dbc.Input(
            className="mb-3 p-2",
            placeholder="Enter Album Name...",
            size="sm",
            valid=True,
            debounce=True,
        ),
    ],
)
