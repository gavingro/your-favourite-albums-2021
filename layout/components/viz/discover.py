from dash.dependencies import Input, Output
import plotly.express as px
from plotly import graph_objects as go

from app import app
from data.data import AOTY_by_album, TOP_COL_LOOKUP
from data.datafunc import get_albums_of_note
from assets.app_colors import APP_COLORS


@app.callback(
    Output("discover-fig", "figure"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def create_discover_fig(user_album_select, top_col):
    # re-rank list
    AOTY_by_album_ranked = (
        AOTY_by_album.sort_values(top_col, ascending=False)
        .reset_index()
        .drop(columns="index")
    )

    # top_10_albums = AOTY_by_album_ranked.loc[
    #     (AOTY_by_album_ranked[TOP_COL_LOOKUP[top_col]] == True)
    #     | (AOTY_by_album_ranked["Album"] == user_album_select)
    # ]

    # top_10_albums.loc[:, "user_album"] = top_10_albums.loc[:, "Album"].apply(
    #     lambda album: True if album == user_album_select else False
    # )

    album_search = [user_album_select] if user_album_select else None
    albums_of_note = get_albums_of_note(AOTY_by_album_ranked, album_search)

    max_submissions = AOTY_by_album["album_submission_count"].max()

    DISCOVER_FIG = px.scatter(
        AOTY_by_album,
        x="album_submission_count",
        y="album_average_rank",
        color=TOP_COL_LOOKUP[top_col],
        size="album_score",
        template="simple_white",
        labels={
            "album_average_rank": "Average Album Rank",
            "album_submission_count": "Album Submission Count",
            TOP_COL_LOOKUP[top_col]: "Top 10",
        },
        custom_data=["Artist", "Album", "album_score"],
        opacity=0.4,
        color_discrete_sequence=[APP_COLORS["standard"], APP_COLORS["accent"]],
    )
    DISCOVER_FIG.update_traces(
        hovertemplate="<br>".join(
            [
                "<b>%{customdata[0]}</b> - <i>%{customdata[1]}</i>",
                "",
                "Average Album Rank: %{y:.2f}",
                "Album Submission Count : %{x}",
                "Album Score: %{customdata[2]}",
                "<extra></extra>",
            ]
        ),
        # marker = {"size" : 12},
        selector=dict(mode="markers"),
    )

    DISCOVER_FIG.add_shape(
        type="line",
        x0=max_submissions / 2,
        y0=0,
        x1=max_submissions / 2,
        y1=10.5,
        line=dict(
            color=APP_COLORS["dark"],
            width=4,
            dash="dash",
        ),
    )
    DISCOVER_FIG.add_shape(
        type="line",
        x0=1,
        y0=5.5,
        x1=max_submissions + 1,
        y1=5.5,
        line=dict(
            color=APP_COLORS["dark"],
            width=4,
            dash="dash",
        ),
    )

    DISCOVER_FIG.add_trace(
        go.Scatter(
            x=[2, 2, max_submissions - 1, max_submissions - 1],
            y=[0, 10.5, 0, 10.5],
            mode="text",
            name="Zones",
            text=[
                "Hidden Gems",
                "Barely Made It",
                "Certified Bangers",
                "Easy Listening",
            ],
            textposition="bottom center",
            textfont={"color": APP_COLORS["dark"], "size": 13},
            showlegend=False,
            hoverinfo="skip",
        )
    )

    for row in range(len(albums_of_note)):
        album = albums_of_note.iloc[row, :]
        DISCOVER_FIG.add_annotation(
            x=int(album["album_submission_count"]),
            y=float(album["album_average_rank"]),
            text=album["Album"],
            font={"color": APP_COLORS["dim"], "size": 9},
        )

    DISCOVER_FIG.update_yaxes(autorange="reversed")
    DISCOVER_FIG.update_layout(
        hovermode="closest",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        dragmode="select",
    )

    return DISCOVER_FIG
