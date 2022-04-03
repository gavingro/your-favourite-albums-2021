import os

import dash
import dash_bootstrap_components as dbc

FONT_AWESOME_LINK = "https://use.fontawesome.com/b38cb1f2da.css"

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.ZEPHYR, FONT_AWESOME_LINK],
    title="Your Favourite Albums 2021",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
