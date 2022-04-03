import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from data.data import AOTY_by_album
from assets.app_colors import APP_COLORS


# Get Album Metadata and populate title based on it
@app.callback(
    Output("discover-table", "columns"),
    Output("discover-table", "data"),
    Output("discover-table", "style_data_conditional"),
    [
        Input("user-album-select", "name"),
        Input("rank-by-radio", "value"),
        Input("discover-fig", "selectedData"),
    ],
)
def update_discover_table(user_album_select, top_col, selected_data):
    # TODO: Update Table to display only those albums selected in Album Discover figure

    # Sort df
    AOTY_by_album_ranked = (
        AOTY_by_album.sort_values(top_col, ascending=False)
        .reset_index()
        .drop(columns="index")
        .reset_index()
    )

    # Data Pipeline
    AOTY_by_album_ranked["Rank"] = AOTY_by_album_ranked["index"] + 1
    AOTY_by_album_ranked["album_average_rank"] = AOTY_by_album_ranked[
        "album_average_rank"
    ].round(2)
    AOTY_display = AOTY_by_album_ranked[
        ["Rank", "Artist", "Album", "album_average_rank", "album_submission_count"]
    ]
    AOTY_display = AOTY_display.rename(
        columns={
            "album_submission_count": "Submission Count",
            "album_average_rank": "Average Album Rank",
        }
    )

    # Get Which Albums to Display
    if selected_data:
        selected_albums = [point["customdata"][1] for point in selected_data["points"]]
        if user_album_select:
            selected_albums.append(user_album_select)

        # selected_albums = selected_data["Album"].values
        AOTY_display = AOTY_display.loc[AOTY_display["Album"].isin(selected_albums)]

    # Export
    columns = [{"name": i, "id": i} for i in AOTY_display.columns]
    data = AOTY_display.to_dict("records")

    # Styling
    conditional_style = [
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "rgb(220, 220, 220)",
        },
        {"if": {"column_type": "numeric"}, "textAlign": "left"},
    ]

    # # This bugged out when I returned to it 4 months later.
    # # Something weird is happening with the underlying javascript.
    # # Causes problems when you select an album to search while
    # # filtering the data table.
    # if user_album_select:
    #     conditional_style.append(
    #         {
    #             "if": {
    #                 "filter_query": f"{{Album}} = {user_album_select}"
    #             },  # needs "{string}" for plotly
    #             "backgroundColor": APP_COLORS["accent"],
    #             "color": "white",
    #         }
    #     )

    return columns, data, conditional_style
