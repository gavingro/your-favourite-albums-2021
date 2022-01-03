import unittest
import pandas as pd

from data.datafunc import (
    trim_2021_df,
    get_total_listers,
    get_total_artists,
    get_total_albums,
    add_submission_count_to_albums,
    add_unique_album_column,
    add_artist_album_release_count,
    add_multi_album_artist_column,
)


class TestDataFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.AOTY2021 = pd.read_csv("data/AOTY-2021-lists.csv")
        cls.KNOWNLISTERCOUNT2021 = 98
        cls.KNOWNARTISTCOUNT2021 = 432
        cls.KNOWNALBUMCOUNT2021 = 439

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
            get_total_artists(TestDataFunc.AOTY2021), TestDataFunc.KNOWNARTISTCOUNT2021
        )

    def test_get_total_albums(self):
        self.assertEqual(
            get_total_albums(TestDataFunc.AOTY2021), TestDataFunc.KNOWNALBUMCOUNT2021
        )

    def test_add_submission_count_to_albums(self):
        self.AOTY2021 = add_submission_count_to_albums(TestDataFunc.AOTY2021)
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
        self.AOTY2021 = add_submission_count_to_albums(TestDataFunc.AOTY2021)
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
        pass

    def test_add_multi_album_artist_column(self):
        pass


if __name__ == "__main__":
    unittest.main()
