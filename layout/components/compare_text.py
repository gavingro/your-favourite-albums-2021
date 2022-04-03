import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html

from app import app
from data.data import AOTY_by_album


# Get Album Metadata and populate title based on it
@app.callback(
    Output("compare-text", "children"),
    [Input("user-album-select", "name")],
)
def get_compare_text(user_album_select):
    if not user_album_select:
        children = html.P(
            className="lead mb-3 mt-3",
            children=[
                "Search for an known album with 'Album Search' in the sidebar to compare it to other albums.",
                html.Br(),
                "Without a specific album to focus on, this page is disorganized.",
                html.Br(),
                "Try 'Hotel TV' or find your own favourite album in the dataset using the Discover tab."
                ],
        )

    else:
        artist = (
            AOTY_by_album.loc[AOTY_by_album["Album"] == user_album_select]
            .loc[:, "Artist"]
            .values[0]
        )
        title_text = " - ".join([artist, user_album_select])

        children = html.H5(
            className="display-6 fw-bold",
            children=[title_text],
        )
        
    return children
