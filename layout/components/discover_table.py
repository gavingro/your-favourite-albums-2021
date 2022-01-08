import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from data.data import AOTY_by_album


# Get Album Metadata and populate title based on it
@app.callback(
    Output("discover-table", "columns"),
    Output("discover-table", "data"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def update_discover_table(user_album_select, top_col):
    # TODO: Update Table to display only those albums selected in Album Discover figure
    columns = [{"name": i, "id": i} for i in AOTY_by_album.columns]
    data = (AOTY_by_album.to_dict("records"),)

    return columns, data
