from dash.dependencies import Input, Output
import plotly.express as px

from app import app
from data.data import AOTY_by_album, TOP_COL_LOOKUP
from assets.app_colors import APP_COLORS


@app.callback(
    Output("top-10-album-count-fig", "figure"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def create_top_10_album_count_fig(user_album_select, top_col):
    # re-rank list
    AOTY_by_album_ranked = (
        AOTY_by_album.sort_values(top_col, ascending=False)
        .reset_index()
        .drop(columns="index")
    )

    top_10_albums = AOTY_by_album_ranked.loc[
        (AOTY_by_album_ranked[TOP_COL_LOOKUP[top_col]] == True)
        | (AOTY_by_album_ranked["Album"] == user_album_select)
    ]

    top_10_albums.loc[:, "user_album"] = top_10_albums.loc[:, "Album"].apply(
        lambda album: True if album == user_album_select else False
    )

    # album_search = [user_album_select] if user_album_select else None
    # albums_of_note = get_albums_of_note(AOTY_by_album_ranked, album_search)

    if user_album_select:
        TOP_10_ALBUM_COUNT_FIG = px.bar(
            top_10_albums,
            x="Album",
            y=["album_submission_count"],
            barmode="stack",
            color="user_album",
            text="Artist",
            hover_name="Album",
            custom_data=["Artist"],
            labels={"value": "Album Submissions"},
            template="simple_white",
            height=375,
            color_discrete_sequence=[APP_COLORS["accent"], APP_COLORS["standard"]],
        )
    else:
        TOP_10_ALBUM_COUNT_FIG = px.bar(
            top_10_albums,
            x="Album",
            y=["album_submission_count"],
            barmode="stack",
            text="Artist",
            hover_name="Album",
            custom_data=["Artist"],
            labels={"value": "Album Submissions", "Album": ""},
            template="simple_white",
            height=375,
            color_discrete_sequence=[APP_COLORS["accent"]],
        )

    TOP_10_ALBUM_COUNT_FIG.update_traces(
        hovertemplate="<br>".join(
            [
                "<b>%{customdata}</b> - <i>%{x}</i>",
                "",
                "<extra></extra>",
            ]
        )
    )

    TOP_10_ALBUM_COUNT_FIG.update_layout(
        hovermode="closest",
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    TOP_10_ALBUM_COUNT_FIG.add_hrect(
        y0=AOTY_by_album_ranked["album_submission_count"].quantile(0.25),
        y1=AOTY_by_album_ranked["album_submission_count"].quantile(0.75),
        opacity=0.3,
        fillcolor=APP_COLORS["dark"],
        annotation_text=f"'Usual' Album Submission Count: {AOTY_by_album_ranked['album_submission_count'].quantile(0.25):.2f} - {AOTY_by_album_ranked['album_score'].quantile(0.75):.2f}",
        annotation_position="inside right",
        annotation_font_color=APP_COLORS["light"],
    )

    TOP_10_ALBUM_COUNT_FIG.update_xaxes(showticklabels=False, visible=False)
    TOP_10_ALBUM_COUNT_FIG.update_yaxes(autorange="reversed")

    return TOP_10_ALBUM_COUNT_FIG
