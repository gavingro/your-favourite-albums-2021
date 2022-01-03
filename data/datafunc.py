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
        Long form AOTY dataframe with Rank and Album column.

    Returns
    -------
    pd.DataFrame
        AOTY dataframe with added album_score column.
    """
    new_df = df.copy()
    new_df["album_score"] = new_df.groupby(["Album"])["Rank"].transform(sum)
    return new_df


def add_submission_count_to_albums(df: pd.DataFrame) -> pd.DataFrame:
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
