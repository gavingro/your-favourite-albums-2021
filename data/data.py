import pandas as pd

from .datafunc import (
    trim_2021_df,
    get_total_listers,
    get_total_artists,
    get_total_albums,
    add_submission_count_to_albums,
    add_unique_album_column,
    add_artist_album_release_count,
    add_multi_album_artist_column,
    add_album_score,
)

AOTY = pd.read_csv("./data/AOTY-2021-lists.csv")
AOTY = (
    AOTY.pipe(trim_2021_df)
    .pipe(add_album_score)
    .pipe(add_submission_count_to_albums)
    .pipe(add_unique_album_column)
    .pipe(add_artist_album_release_count)
    .pipe(add_multi_album_artist_column)
)

TOTAL_LISTERS = get_total_listers(AOTY)
TOTAL_ARTISTS = get_total_artists(AOTY)
TOTAL_ALBUMS = get_total_albums(AOTY)

if __name__ == "__main__":
    print(AOTY)
