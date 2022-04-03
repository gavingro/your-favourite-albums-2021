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
                            href="/",
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
        dbc.Label(
            children = [
                "Rank By:",
                html.Span("[?]",
                          style = {"textDecoration": "underline", "cursor": "pointer"},
                          className = "px-2"),
                html.I(
                    className = "fa-solid fa-circle-info",
                    style = {"color" : "white"},
                )
            ],
            id = "rank-by-tooltip"
        ),
        dbc.Tooltip(
            children = [
                "When gathering this data, each participant ranked 10 of their favourite 2021 albums in order.",
                html.Hr(),
                html.Span("Weighted Album Score ", className="font-italic"),
                "awards points to each album based on how high ranking that album was on each top 10 list: a #1 album is awarded 10 points while a #10 album is only awarded 1 point.",
                html.Br(),
                html.Br(),
                html.Span("Total Album Submissions ", className="font-italic"),
                "ignores these rankings, and judges only the number of top 10 lists an album appears on."
            ],
            placement = "right",
            target = "rank-by-tooltip"
        ),
        dbc.RadioItems(
            options=[
                {"label": "Weighted Album Score", "value": "album_score"},
                {"label": "Total Album Submissions", "value": "album_submission_count"},
            ],
            value="album_score",
            id="rank-by-radio",
        ),
        dbc.Label("Album Search:", class_name="mt-3"),
        USER_ALBUM_INPUT,
    ],
)
