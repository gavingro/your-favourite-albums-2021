import dash_bootstrap_components as dbc
from dash import html

from .user_album_input import USER_ALBUM_INPUT

SIDEBAR = dbc.Col(
    class_name="d-flex flex-column flex-shrink-1 p-4 text-white bg-dark sticky-md-top rounded-right",
    style={"height": "100vh"},
    children=[
        html.A(
            className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none",
            href="/",
            children=[
                html.Img(className="bi me-2", height=44, src="assets/cd_icon.png"),
                html.Span(
                    className="fs-4 fw-bold lh-1",
                    children=["Your Favourite", html.Br(), "Albums 2021"],
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
                            active="exact",
                            href="/home",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=22,
                                    width=22,
                                    src="assets/home-icon.png",
                                ),
                                html.Span(
                                    className="fs-6 fw-light p-3", children="Home"
                                ),
                            ],
                        )
                    ]
                ),
                dbc.NavItem(
                    children=[
                        dbc.NavLink(
                            active="exact",
                            href="/top_10",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=22,
                                    width=22,
                                    src="assets/podium-icon.png",
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
                            active="exact",
                            href="/discover",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=22,
                                    width=22,
                                    src="assets/discover-icon.png",
                                ),
                                html.Span(
                                    className="fs-6 fw-light p-3", children="Discover"
                                ),
                            ],
                        )
                    ]
                ),
                dbc.NavItem(
                    children=[
                        dbc.NavLink(
                            active="exact",
                            href="/compare",
                            children=[
                                html.Img(
                                    className="bi me-2",
                                    height=22,
                                    width=22,
                                    src="assets/compare-icon.png",
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
        dbc.Label("Rank By:"),
        dbc.RadioItems(
            options=[
                {"label": "Album Score", "value": "album_score"},
                {"label": "Album Submissions", "value": "album_submission_count"},
            ],
            value="album_score",
            id="rank-by-radio",
        ),
        dbc.Label("Album Search:", class_name="mt-3"),
        USER_ALBUM_INPUT,
    ],
)
