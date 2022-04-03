from dash.dependencies import Input, Output, State
import numpy as np

from app import app
from data.data import AOTY_by_album, TOP_COL_LOOKUP

# Component Callbacks
from .components.compare_text import get_compare_text
from .components.discover_text import get_discover_text
from .components.discover_table import update_discover_table

# Viz Callback Updates
from .components.viz.top_10_album_score import create_top_10_album_score_fig
from .components.viz.top_10_album_count import create_top_10_album_count_fig
from .components.viz.discover import create_discover_fig
from .components.viz.user_stripplot import create_user_stripplot_fig
from .components.viz.user_rank import create_user_rank_fig
from .components.viz.user_score_compare import create_user_score_compare_fig
from .components.viz.user_count_compare import create_user_count_compare_fig


# Create ranked_album_df by Radio Select
@app.callback(Output("ranked-album-df", "children"), [Input("rank-by-radio", "value")])
def create_ranked_album_df_by_radio_select(COLUMN):
    ranked_AOTY_by_album = (
        AOTY_by_album.sort_values(COLUMN, ascending=False)
        .reset_index()
        .drop(columns="index")
    )
    return ranked_AOTY_by_album


# Create top_10_album list by output of ranked_album_df
@app.callback(
    Output("top-10-album-df", "children"),
    [Input("ranked-album-df", "value"), Input("rank-by-radio", "value")],
)
def get_top_10_albums_from_rankings(ranked_album_df, COLUMN):
    top_10_album_df = ranked_album_df.loc[
        ranked_album_df[TOP_COL_LOOKUP[COLUMN]] == True
    ]
    return top_10_album_df


# Validate User Album Selection
@app.callback(
    Output("user-album-select", "name"),
    Output("user-album-select", "valid"),
    Output("user-album-select", "invalid"),
    [
        State("user-album-select", "value"),
        State("user-album-select", "name"),
        Input("user-album-select", "n_submit"),
    ],
)
def validate_user_album_selection(user_album_try, old_user_album, n_submits):
    # check if actual album, return none if empty, and
    # stop update of name if not

    if not user_album_try:
        return None, False, False

    known_albums = AOTY_by_album["Album"].values

    user_album_validity = user_album_try in known_albums
    if user_album_validity:
        user_album_selection = user_album_try
    else:
        user_album_selection = old_user_album
    return user_album_selection, user_album_validity, not user_album_validity


@app.callback(
    Output("top-10-ranked-by", "children"),
    Input("rank-by-radio", "value"),
)
def update_top_10_ranking(rank_by):
    if rank_by == "album_submission_count":
        ranked_by = "Total Album Submissions"
    else:
        ranked_by = "Weighted Album Score"
    return ranked_by