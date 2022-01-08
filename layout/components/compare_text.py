import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html

from app import app
from data.data import AOTY_by_album


# Get Album Metadata and populate title based on it
@app.callback(
    Output("compare-text", "children"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def get_compare_text(user_album_select, top_col):
    if not user_album_select:
        title_text = "Search for an known album in the sidebar to compare to the overall and top album submissions."

    else:
        artist = (
            AOTY_by_album.loc[AOTY_by_album["Album"] == user_album_select]
            .loc[:, "Artist"]
            .values[0]
        )
        title_text = " - ".join([artist, user_album_select])

    children = html.P(
        className="lead mb-3 mt-3",
        children=[title_text],
    )
    return children
