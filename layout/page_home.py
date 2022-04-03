from dash import html
import dash_bootstrap_components as dbc


SPOTIFY_LINK = "https://open.spotify.com/playlist/1JaWG6CdqroFJmq7OcJ1J8?si=8699cc89fd764447&fbclid=IwAR2Iz-6vfRUPVOHDFbtkt2WxUzF0ewzyTdcXBZ5NPGsIYlgxvM7N6t86zt4&nd=1"
APPLE_LINK = "https://music.apple.com/ca/playlist/your-top-albums-2k21/pl.u-leylWDLfjxB95jV?fbclid=IwAR1bd-vEUGjB_A731LJRZO-n2c-LJp8m_Y-zZDacBQ6tAYp722NbX9A98M8"

HOME_PAGE = html.Div(
    className="px-4 pt-5 my-5 text-center border-bottom",
    children=[
        html.H1(className="display-4 fw-bold", children="Your Favourite Albums"),
        dbc.Col(
            className="mx-auto",
            lg=6,
            children=[
                html.P(
                    className="lead mb-4",
                    children=[
                        "A 'best-of-the-best' collection of albums assembled by people who care based on the results of a \"Top 10 Albums\" survey between friends.",
                        html.Br(),
                        html.Br(),
                        "Use the sidebar to explore the winners, discover new albums, and compare your own favourites.",
                        html.Br(),
                        html.Br(),
                        "Playlists to explore the music made available through:"
                    ],
                ),
                html.Div(
                    className="d-grid gap-2 d-sm-flex justify-content-sm-center mb-5",
                    children=[
                        dbc.Button(
                            class_name="px-4 me-sm-3",
                            size="lg",
                            color="primary",
                            children="Spotify",
                            href=SPOTIFY_LINK,
                            target="_blank",
                        ),
                        dbc.Button(
                            class_name="px-4 me-sm-3",
                            size="lg",
                            color="primary",
                            children="Apple Music",
                            href=APPLE_LINK,
                            target="_blank",
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="overflow-hidden",
            style={"max-height": "30vh"},
            children=[
                dbc.Container(
                    class_name="px-5",
                    children=[
                        html.Img(
                            className="img-fluid border rounded-3 shadow-lg mb-4",
                            src="assets/album_spread.jpg",
                        )
                    ],
                )
            ],
        ),
    ],
)
