from dash import html
import dash_bootstrap_components as dbc

from app import app
from data.data import AOTY_by_album

known_albums = html.Datalist(
    id="known-albums",
    children=[html.Option(value=album) for album in AOTY_by_album["Album"].values],
)

USER_ALBUM_INPUT = dbc.Input(
    className="mb-3 p-2",
    placeholder="Enter Album Name...",
    size="sm",
    autoComplete="on",
    persistence=True,
    persistence_type="session",
    n_submit=0,
    list="known-albums",
    name=None,
    debounce=True,
    id="user-album-select",
)
