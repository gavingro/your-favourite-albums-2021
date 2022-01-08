from dash.dependencies import Input, Output
import plotly.express as px
from numpy.random import choice

from app import app
from data.data import AOTY, AOTY_by_album, TOP_COL_LOOKUP
from data.datafunc import get_competing_albums
from assets.app_colors import APP_COLORS


@app.callback(
    Output("user-rank-fig", "figure"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def create_user_rank_fig(user_album_select, top_col):
    # get random album if none are selected
    if not user_album_select:
        album_list = AOTY_by_album["Album"].values
        user_album_select = choice(album_list)

    # re-rank list
    AOTY_by_album_ranked = (
        AOTY_by_album.sort_values(top_col, ascending=False)
        .reset_index()
        .drop(columns="index")
        .reset_index()
    )
    AOTY_by_album_ranked["rank"] = AOTY_by_album_ranked["index"] + 1

    AOTY_by_album_ranked.loc[:, "user_album"] = AOTY_by_album_ranked.loc[
        :, "Album"
    ].apply(lambda album: True if album == user_album_select else False)

    nearby_df = get_competing_albums(AOTY_by_album_ranked, user_album_select)

    USER_RANK_FIG = px.bar(
        data_frame=nearby_df,
        x="Album",
        y=top_col,
        color="user_album",
        custom_data=[
            nearby_df.index + 1,
            "Artist",
            "album_score",
            "album_submission_count",
        ],
        labels={
            "album_score": "Album Score",
            "album_submission_count": "Album Submission Count",
            "Album": "",
        },
        template="simple_white",
        text="rank",
        color_discrete_map={True: APP_COLORS["accent"], False: APP_COLORS["standard"]},
    )

    USER_RANK_FIG.update_traces(
        hovertemplate="<br>".join(
            [
                "<b>Rank %{customdata[0]}:</b>",
                "%{customdata[1]} - <i>%{x}</i>",
                "",
                "Total Score: %{customdata[2]}",
                "Submission Count: %{customdata[3]}",
                "<extra></extra>",
            ]
        )
    )

    USER_RANK_FIG.update_layout(
        hovermode="closest", showlegend=False, xaxis_categoryorder="total descending"
    )
    USER_RANK_FIG.update_yaxes(
        side="right",
    )

    return USER_RANK_FIG
