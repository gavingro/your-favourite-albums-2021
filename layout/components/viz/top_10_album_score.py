import plotly.express as px

from data.data import AOTY_by_album
from data.datafunc import get_albums_of_note
from assets.app_colors import APP_COLORS

# to fix and move later
COLUMN = "album_score"
USER_ALBUM = "Hotel TV"

TOP_COL_LOOKUP = {
    "album_score": "top_10_score_album",
    "album_submission_count": "top_10_count_album",
}

AOTY_by_album = (
    AOTY_by_album.sort_values(COLUMN, ascending=False)
    .reset_index()
    .drop(columns="index")
)

top_10_albums = AOTY_by_album.loc[AOTY_by_album[TOP_COL_LOOKUP[COLUMN]] == True]

album_search = [USER_ALBUM] if USER_ALBUM else None
albums_of_note = get_albums_of_note(AOTY_by_album, album_search)

# viz
TOP_10_ALBUM_SCORE_FIG = px.bar(
    top_10_albums,
    x="Album",
    y=["album_score"],
    barmode="group",
    text_auto=True,
    hover_name="Album",
    custom_data=["Artist"],
    labels={"value": "Album Score"},
    template="simple_white",
    height=375,
    color_discrete_sequence=[APP_COLORS["standard"]],
)
TOP_10_ALBUM_SCORE_FIG.update_traces(
    hovertemplate="<br>".join(
        [
            "<b>%{customdata}</b> - <i>%{x}</i>",
            "",
            "<extra></extra>",
        ]
    )
)
TOP_10_ALBUM_SCORE_FIG.update_layout(hovermode="closest", showlegend=False)

TOP_10_ALBUM_SCORE_FIG.add_hrect(
    y0=AOTY_by_album["album_score"].quantile(0.25),
    y1=AOTY_by_album["album_score"].quantile(0.75),
    opacity=0.3,
    fillcolor=APP_COLORS["dark"],
    annotation_text=f"'Usual' Album scores: {AOTY_by_album['album_score'].quantile(0.25):.2f} - {AOTY_by_album['album_score'].quantile(0.75):.2f}",
    annotation_position="inside right",
    annotation_font_color=APP_COLORS["light"],
)
