from dash.dependencies import Input, Output
import plotly.express as px
from numpy.random import choice

from app import app
from data.data import AOTY_by_album, TOP_COL_LOOKUP
from assets.app_colors import APP_COLORS


@app.callback(
    Output("user-count-compare-fig", "figure"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def create_user_count_compare_fig(user_album_select, top_col):
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

    top_10_albums = AOTY_by_album_ranked.loc[
        (AOTY_by_album_ranked[TOP_COL_LOOKUP[top_col]] == True)
        | (AOTY_by_album_ranked["Album"] == user_album_select)
    ]

    compare_df = AOTY_by_album_ranked.loc[
        (AOTY_by_album_ranked["Album"] == user_album_select)
        | (
            AOTY_by_album_ranked["album_score"]
            == AOTY_by_album_ranked["album_score"].max()
        )
    ]

    compare_df["album_average_rank"] = 0 - compare_df["album_average_rank"]

    # figure
    USER_COUNT_COMPARE_FIG = px.bar(
        data_frame=compare_df,
        x="Album",
        y="album_average_rank",
        color="user_album",
        custom_data=["Artist", "album_score", "album_submission_count"],
        labels={
            "album_average_rank": "Average Album Voter Rank<br><i>(Lower is Better)</i>",
            "Album": "",
        },
        template="simple_white",
        text="rank",
        color_discrete_map={True: APP_COLORS["accent"], False: APP_COLORS["standard"]},
    )

    USER_COUNT_COMPARE_FIG.update_traces(
        base=10,
        hovertemplate="<br>".join(
            [
                "<b>%{customdata[0]}</b> - <i>%{x}</i>",
                "",
                "<extra></extra>",
            ]
        ),
    )

    # overall average
    overall_average = 5.5  # AOTY_by_album["album_average_rank"].mean()
    USER_COUNT_COMPARE_FIG.add_hrect(
        y0=overall_average - 0.05,
        y1=overall_average + 0.05,
        opacity=0.3,
        fillcolor=APP_COLORS["dark"],
        annotation_text="Overall Average",
        annotation_font={"size": 8},
        annotation_position="outside left",
        annotation_font_color=APP_COLORS["dim"],
    )

    # top 10 average
    top_10_average = top_10_albums["album_average_rank"].mean()
    USER_COUNT_COMPARE_FIG.add_hrect(
        y0=top_10_average - 0.05,
        y1=top_10_average + 0.05,
        opacity=0.3,
        fillcolor=APP_COLORS["dark"],
        annotation_text="Top 10 Average",
        annotation_font={"size": 8},
        annotation_position="outside left",
        annotation_font_color=APP_COLORS["dim"],
    )

    # Add invisible points for hover
    USER_COUNT_COMPARE_FIG.add_scatter(
        x=[user_album_select, user_album_select],
        y=[overall_average, top_10_average],
        showlegend=False,
        hoverinfo="y",
        mode="none",
    )

    USER_COUNT_COMPARE_FIG.update_yaxes(range=[10, 0], tick0=1, side="right")

    USER_COUNT_COMPARE_FIG.update_layout(
        hovermode="y", showlegend=False, xaxis_categoryorder="trace"
    )

    return USER_COUNT_COMPARE_FIG
