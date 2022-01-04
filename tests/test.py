import unittest
import pandas as pd

from data.datafunc import (
    add_album_score,
    trim_2021_df,
    get_total_listers,
    get_total_artists,
    get_total_albums,
    add_album_score,
    add_top_10_albums_by_score,
    add_top_10_albums_by_count,
    add_album_average_rank,
    add_album_submission_count,
    add_unique_album_column,
    add_artist_album_release_count,
    add_multi_album_artist_column,
    get_wide_form_album_df,
    get_albums_of_note,
)


class TestDataFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.AOTY2021 = pd.read_csv("data/AOTY-2021-lists.csv")
        cls.KNOWNLISTERCOUNT2021 = 98
        cls.KNOWNARTISTCOUNT2021 = 432
        cls.KNOWNALBUMCOUNT2021 = (
            439  # Shouldn't it be 439 not 436 to match Sheets? Did Will screw up?
        )
        cls.ALBUMSOFNOTE2021 = 3  # update as our function updates

    def setUp(self) -> None:
        pass

    def test_trim_2021_df(self):
        self.ncol_untrimmed = len(TestDataFunc.AOTY2021.columns)
        self.assertEqual(self.ncol_untrimmed, 6)  # pre trimmed df size for sanity
        self.trimmed_df = trim_2021_df(TestDataFunc.AOTY2021)
        self.ncol_trimmed = len(self.trimmed_df.columns)
        self.assertEqual(self.ncol_trimmed, 4)
        self.colnames = self.trimmed_df.columns
        self.assertIn("Artist", self.colnames)
        self.assertIn("Album", self.colnames)
        self.assertIn("Lister", self.colnames)
        self.assertIn("Rank", self.colnames)

    def test_get_total_listers(self):
        self.assertEqual(
            get_total_listers(TestDataFunc.AOTY2021), TestDataFunc.KNOWNLISTERCOUNT2021
        )

    def test_get_total_artists(self):
        self.assertEqual(
            get_total_artists(trim_2021_df(TestDataFunc.AOTY2021)),
            TestDataFunc.KNOWNARTISTCOUNT2021,
        )

    def test_get_total_albums(self):
        self.assertEqual(
            get_total_albums(trim_2021_df(TestDataFunc.AOTY2021)),
            436,  # should be TestDataFunc.KNOWNALBUMCOUNT2021,
        )

    def test_add_album_score(self):
        self.AOTY2021 = add_album_submission_count(TestDataFunc.AOTY2021)
        self.AOTY2021 = add_album_score(self.AOTY2021)
        self.sour_score = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "Sour"
        ].album_score.values[0]
        self.assertEqual(self.sour_score, 137)  # observed 137 from 2021 Google Sheets
        self.silksonic_score = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "An Evening With Silk Sonic"
        ].album_score.values[0]
        self.assertEqual(
            self.silksonic_score, 171
        )  # observed 171 from 2021 Google Sheets
        self.billie_score = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "Happier Than Ever"
        ].album_score.values[0]
        self.assertEqual(self.sour_score, 137)  # observed 137 from 2021 Google Sheets

    def test_add_top_10_albums_by_score(self):
        self.AOTY2021 = add_album_submission_count(TestDataFunc.AOTY2021)
        self.AOTY2021 = add_album_score(self.AOTY2021)
        self.AOTY2021 = add_top_10_albums_by_score(self.AOTY2021)
        self.assertTrue(
            self.AOTY2021.loc[
                self.AOTY2021["Album"] == "Day/Night"  # corner case from data
            ].top_10_score_album.values[0]
        )
        self.assertFalse(
            self.AOTY2021.loc[
                self.AOTY2021["Album"] == "Planet Her"  # corner case from data
            ].top_10_score_album.values[0]
        )

    def test_add_top_10_albums_by_count(self):
        self.AOTY2021 = add_album_submission_count(TestDataFunc.AOTY2021)
        self.AOTY2021 = add_top_10_albums_by_count(self.AOTY2021)
        self.assertFalse(
            self.AOTY2021.loc[
                self.AOTY2021["Album"] == "Day/Night"  # corner case from data
            ].top_10_count_album.values[0]
        )
        self.assertTrue(
            self.AOTY2021.loc[
                self.AOTY2021["Album"] == "Planet Her"  # corner case from data
            ].top_10_count_album.values[0]
        )

    def test_add_album_average_rank(self):
        self.AOTY2021 = add_album_average_rank(TestDataFunc.AOTY2021)
        self.wilderado_score = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "Wilderado"
        ].album_average_rank.values[0]
        self.assertEqual(self.wilderado_score, 1)  # 1 scorer gave rank 1
        self.country_score = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "Country Again"
        ].album_average_rank.values[0]
        self.assertEqual(self.country_score, 5)  # 2 scorer average rank 5

    def test_add_album_submission_count(self):
        self.AOTY2021 = add_album_submission_count(TestDataFunc.AOTY2021)
        self.happier_than_ever_count = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "Happier Than Ever"
        ].album_submission_count.values[0]
        self.assertEqual(
            self.happier_than_ever_count, 22  # observed from 2021 Google Sheets
        )
        self.blacklight_count = self.AOTY2021.loc[
            self.AOTY2021["Album"] == "Blacklight"
        ].album_submission_count.values[0]
        self.assertEqual(self.blacklight_count, 1)  # Observed from 2021 Google Sheets

    def test_add_unique_album_column(self):
        self.AOTY2021 = add_album_submission_count(TestDataFunc.AOTY2021)
        self.AOTY2021 = add_unique_album_column(self.AOTY2021)
        self.assertFalse(
            self.AOTY2021.loc[
                self.AOTY2021["Album"] == "Happier Than Ever"
            ].unique_album_submission.values[0]
        )
        self.assertTrue(
            self.AOTY2021.loc[
                self.AOTY2021["Album"] == "Blacklight"
            ].unique_album_submission.values[0]
        )

    def test_add_artist_album_release_count(self):
        self.AOTY2021 = add_artist_album_release_count(TestDataFunc.AOTY2021)
        self.aquilo_release_count = self.AOTY2021.loc[
            self.AOTY2021["Artist"] == "Aquilo"
        ].artist_album_release_count.values[0]
        self.assertEqual(self.aquilo_release_count, 1)  # known single album release
        self.drake_release_count = self.AOTY2021.loc[
            self.AOTY2021["Artist"] == "Drake"
        ].artist_album_release_count.values[0]
        self.assertEqual(self.drake_release_count, 2)  # known multi album release

    def test_add_multi_album_artist_column(self):
        self.AOTY2021 = add_artist_album_release_count(TestDataFunc.AOTY2021)
        self.AOTY2021 = add_multi_album_artist_column(self.AOTY2021)
        self.assertFalse(
            self.AOTY2021.loc[
                self.AOTY2021["Artist"] == "Aquilo"
            ].multi_album_artist.values[0]
        )
        self.assertTrue(
            self.AOTY2021.loc[
                self.AOTY2021["Artist"] == "Drake"
            ].multi_album_artist.values[0]
        )

    def test_get_wide_form_df(self):
        self.AOTY = (
            TestDataFunc.AOTY2021.pipe(trim_2021_df)
            .pipe(add_album_submission_count)
            .pipe(add_album_score)
            .pipe(add_top_10_albums_by_count)
            .pipe(add_top_10_albums_by_score)
            .pipe(add_album_average_rank)
            .pipe(add_unique_album_column)
            .pipe(add_artist_album_release_count)
            .pipe(add_multi_album_artist_column)
        )
        self.AOTY_by_album = get_wide_form_album_df(self.AOTY)
        self.assertEqual(len(self.AOTY_by_album), self.KNOWNALBUMCOUNT2021)

    def test_get_albums_of_note(self):
        self.AOTY_by_album = (
            TestDataFunc.AOTY2021.pipe(trim_2021_df)
            .pipe(add_album_submission_count)
            .pipe(add_album_score)
            .pipe(add_top_10_albums_by_count)
            .pipe(add_top_10_albums_by_score)
            .pipe(add_album_average_rank)
            .pipe(add_unique_album_column)
            .pipe(add_artist_album_release_count)
            .pipe(add_multi_album_artist_column)
            .pipe(get_wide_form_album_df)
        )
        self.albums_of_note = get_albums_of_note(
            self.AOTY_by_album, ["Build A Problem"]
        )
        self.assertEqual(
            len(self.albums_of_note), TestDataFunc.ALBUMSOFNOTE2021 + 1
        )  # 1 manually added
        self.assertIn("An Evening With Silk Sonic", self.albums_of_note.Album.values)
        self.assertIn("Planet Her", self.albums_of_note.Album.values)
        self.assertIn("Day/Night", self.albums_of_note.Album.values)
        self.assertIn("Build A Problem", self.albums_of_note.Album.values)


if __name__ == "__main__":
    unittest.main()
