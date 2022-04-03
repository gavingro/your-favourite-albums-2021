import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html

from app import app
from data.data import AOTY_by_album


# Get Album Metadata and populate title based on it
@app.callback(
    Output("discover-text", "children"),
    [Input("discover-fig", "selectedData")],
)
def get_discover_text(user_album_select):
    if not user_album_select:
        title_text = "Drag graph to filter albums."
        

    else:
        title_text = "Enter album name in 'Album Search' to display it on the graph."

    children = html.P(
            className="lead mb-3 mt-3",
            children=[title_text],
        )
    
    return children
