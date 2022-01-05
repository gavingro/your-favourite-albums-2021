import pandas as pd


def trim_2021_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the proper columns only from the 2021 dataframe
    created from the 2021 csv file.

    Parameters
    ----------
    df : pd.DataFrame
        2021 rough df with extra columns from csv file.

    Returns
    -------
    pd.DataFrame
        2021 dataframe of just the relevent columns.
    """
    new_df = df.copy()
    return new_df.iloc[:, :4]


def get_total_listers(df: pd.DataFrame) -> int:
    """
    Returns the total number of unique values from the "lister"
    column of the passed in dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        The long-form AOTY dataframe with a Lister column.

    Returns
    -------
    int
        Count of unique listers.
    """
    new_df = df.copy()
    return new_df["Lister"].nunique()


def get_total_artists(df: pd.DataFrame) -> int:
    """
    Returns the total number of unique values from the "Artist"
    column of the passed in dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        The long-form AOTY dataframe with a Artist column.

    Returns
    -------
    int
        Count of unique artists.
    """
    new_df = df.copy()
    return new_df["Artist"].nunique()


def get_total_albums(df: pd.DataFrame) -> int:
    """
    Returns the total number of unique values from the "Album"
    column of the passed in dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        The long-form AOTY dataframe with a Album column.

    Returns
    -------
    int
        Count of unique albums.
    """
    new_df = df.copy()
    return new_df["Album"].nunique()


def add_album_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds the total album score column to the dataframe
    based on the sum of all the Rank scores.

    Parameters
    ----------
    df : pd.DataFrame
        Long form AOTY dataframe with Rank and Album, and album_submission_count column.

    Returns
    -------
    pd.DataFrame
        AOTY dataframe with added album_score column.
    """
    new_df = df.copy()
    new_df["album_score"] = (11 * new_df["album_submission_count"]) - (
        new_df.groupby(["Album"])["Rank"].transform(sum)
    )
    return new_df


def add_top_10_albums_by_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a boolean column based on if the album is one of the top 10 albums
    of the year by it's album score.

    Parameters
    ----------
    df : pd.DataFrame
        The long form AOTY dataframe (not grouped by album) with
        album_score column.

    Returns
    -------
    pd.DataFrame
        The long form AOTY df with an added
        top_10_score_album column.
    """
    new_df = df.copy()
    top_10_albums = (
        new_df[["Album", "album_score"]]
        .groupby("Album")
        .mean()
        .sort_values("album_score", ascending=False)
        .head(10)
    )
    top_10_album_names = top_10_albums.index.values
    new_df["top_10_score_album"] = new_df["Album"].apply(
        lambda album: True if album in top_10_album_names else False
    )
    return new_df


def add_album_average_rank(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds the album average score column to the dataframe
    based on the average of all the Rank scores for that album.

    Parameters
    ----------
    df : pd.DataFrame
        Long form AOTY dataframe with Rank and Album columns.

    Returns
    -------
    pd.DataFrame
        AOTY dataframe with added album_average_rank column.
    """
    new_df = df.copy()
    new_df["album_average_rank"] = new_df.groupby(["Album"])["Rank"].transform("mean")
    return new_df


def add_album_submission_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a count of how many times each album was submitted in the overall
    data frame.

    Parameters
    ----------
    df : pd.DataFrame
        The AOTY dataframe (Still long form).

    Returns
    -------
    pd.DataFrame
        The AOTY dataframe with an added album_submission_count column.
    """
    new_df = df.copy()
    new_df["album_submission_count"] = new_df.groupby(["Album"])["Album"].transform(
        "size"
    )
    return new_df


def add_top_10_albums_by_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a boolean column based on if the album is one of the top 10 albums
    of the year by it's album submission count.

    Parameters
    ----------
    df : pd.DataFrame
        The long form AOTY dataframe (not grouped by album) with
        album_submission_count column.

    Returns
    -------
    pd.DataFrame
        The long form AOTY df with an added
        top_10_count_album column.
    """
    new_df = df.copy()
    top_10_albums = (
        new_df[["Album", "album_submission_count"]]
        .groupby("Album")
        .mean()
        .sort_values("album_submission_count", ascending=False)
        .head(10)
    )
    top_10_album_names = top_10_albums.index.values
    new_df["top_10_count_album"] = new_df["Album"].apply(
        lambda album: True if album in top_10_album_names else False
    )
    return new_df


def add_unique_album_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a boolean column indicating if an album is uniquely submitted
    (only 1 submission) or not.

    Parameters
    ----------
    df : pd.DataFrame
        The AOTY dataframe WITH album_submission_count column.

    Returns
    -------
    pd.DataFrame
        The AOTY dataframe with added "unique_album_submission" column.
    """
    new_df = df.copy()
    new_df["unique_album_submission"] = new_df["album_submission_count"].apply(
        lambda count: True if count == 1 else False
    )
    return new_df


def add_artist_album_release_count(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds the count to each row of the total number of albums each artist
    is mentioned in on the list.

    Parameters
    ----------
    df : pd.DataFrame
        The AOTY dataframe.

    Returns
    -------
    pd.DataFrame
        The AOTY dataframe with an added album release count column
        unique for each artist.
    """
    new_df = df.copy()
    new_df["artist_album_release_count"] = (
        new_df[["Artist", "Album"]].groupby("Artist")["Album"].transform("nunique")
    )
    return new_df


def add_multi_album_artist_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a boolean column indicating if an artist has released more
    than 1 album on this list this year.

    Parameters
    ----------
    df : pd.DataFrame
        The AOTY dataframe WITH artist_album_release_count column.

    Returns
    -------
    pd.DataFrame
        The AOTY dataframe with added "multi_album_artist" column.
    """
    new_df = df.copy()
    new_df["multi_album_artist"] = new_df["artist_album_release_count"].apply(
        lambda count: False if count == 1 else True
    )
    return new_df


def get_wide_form_album_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Groups the long-form submission dataframe into
    it's relevent features by album.

    Parameters
    ----------
    df : pd.DataFrame
        The long-form AOTY submission df.

    Returns
    -------
    pd.Dataframe
        The wide-form AOTY df grouped by Artist-Album.
    """
    new_df = df.copy()

    relevent_album_columns = [
        "Artist",
        "Album",
        "album_score",
        "album_average_rank",
        "album_submission_count",
        "top_10_score_album",
        "top_10_count_album",
        "unique_album_submission",
        "artist_album_release_count",
        "multi_album_artist",
    ]
    # Each is already added accurately to the long form data with .transform(),
    # so the mean() will maintain the same value going forward.
    album_df = new_df[relevent_album_columns].groupby(["Artist", "Album"]).mean()

    # avoid index cols and set int as the default.
    col_types = {col_name: "int" for col_name in relevent_album_columns[2:]}
    # Adjust specific datatypes
    col_types["album_average_rank"] = "float"
    col_types["unique_album_submission"] = "bool"
    col_types["multi_album_artist"] = "bool"
    col_types["top_10_score_album"] = "bool"
    col_types["top_10_count_album"] = "bool"

    album_df = album_df.astype(col_types).reset_index()
    return album_df


def get_albums_of_note(
    df: pd.DataFrame, extra_albums: list[str] = None
) -> pd.DataFrame:
    """
    Returns a smaller subset of the dataframe with only
    the albums of note to annotate in figures.

    Currently finds:
        - the top album of the year
        - albums that are top scorers or counters but not both

    Parameters
    ----------
    df : pd.DataFrame
        AOTY by album dataframe (wide-form).
    extra_albums : list[str]
        Extra user_defined albums of note to add
        (used mainly with user album lookups)

    Returns
    -------
    pd.DataFrame
        Smaller dataframe of only the relevent albums.
    """
    if not extra_albums:
        extra_albums = []
    albums_of_note = df.copy().loc[
        # Get Top Album
        (df["album_score"] == df["album_score"].max())
        # Get Corner Cases on Top 10 List.
        | ((df["top_10_score_album"] == True) & (df["top_10_count_album"] == False))
        | ((df["top_10_score_album"] == False) & (df["top_10_count_album"] == True))
        # get extra_albums
        | (df["Album"].isin(extra_albums))
    ]
    return albums_of_note
