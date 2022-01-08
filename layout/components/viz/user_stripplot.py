from dash.dependencies import Input, Output
import plotly.express as px
from numpy.random import choice

from app import app
from data.data import AOTY, AOTY_by_album, TOP_COL_LOOKUP
from assets.app_colors import APP_COLORS


@app.callback(
    Output("user-stripplot-fig", "figure"),
    [Input("user-album-select", "name"), Input("rank-by-radio", "value")],
)
def create_user_stripplot_fig(user_album_select, top_col):

    if not user_album_select:
        album_list = AOTY_by_album["Album"].values
        user_album_select = choice(album_list)

    # re-rank list
    AOTY_by_album_ranked = (
        AOTY_by_album.sort_values(top_col, ascending=False)
        .reset_index()
        .drop(columns="index")
    )

    top_10_albums = AOTY_by_album_ranked.loc[
        (AOTY_by_album_ranked[TOP_COL_LOOKUP[top_col]] == True)
    ]

    top_10_albums.loc[:, "user_album"] = top_10_albums.loc[:, "Album"].apply(
        lambda album: True if album == user_album_select else False
    )

    user_album_votes = AOTY.loc[AOTY["Album"] == user_album_select]
    avg_album_rank = user_album_votes["Rank"].mean()

    USER_STRIPPLOT = px.strip(
        data_frame=user_album_votes,
        x="Album",
        y="Rank",
        color="Artist",
        custom_data=["Artist"],
        labels={"Rank": "Rankings on Voters Top 10 Lists", "Artist": ""},
        template="simple_white",
        color_discrete_sequence=[APP_COLORS["standard"], APP_COLORS["accent"]],
        height=350,
    )

    USER_STRIPPLOT.update_traces(
        hovertemplate="<br>".join(
            [
                "<b>%{customdata}</b> - <i>%{x}</i>",
                "",
                f"<b>Total Submissions: {len(user_album_votes)}",
                "<extra></extra>",
            ]
        ),
    )

    # add average album rank
    USER_STRIPPLOT.add_shape(
        type="line",
        x0=-0.4,
        y0=avg_album_rank,
        x1=0.4,
        y1=avg_album_rank,
        name="Average Rank",
        line=dict(
            color=APP_COLORS["dark"],
            width=2,
            dash="dash",
        ),
    )
    USER_STRIPPLOT.add_scatter(
        x=[user_album_select],
        y=[avg_album_rank],
        text="Average Rank",
        textposition="bottom center",
        textfont={"color": APP_COLORS["dim"], "size": 8},
        showlegend=False,
        hoverinfo="y",
        mode="text",
    )

    USER_STRIPPLOT.update_layout(
        hovermode="y",
        xaxis={"visible": False, "showticklabels": False},
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    USER_STRIPPLOT.update_yaxes(range=[11, 0])

    return USER_STRIPPLOT
