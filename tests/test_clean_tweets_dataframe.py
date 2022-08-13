import os
import sys
import unittest

import numpy
import pandas as pd
from clean_tweets_dataframe import Clean_Tweets
from pandas._libs.tslibs.timestamps import Timestamp


# df = pd.read_csv('sample.csv')
class TestTweetDfClean(unittest.TestCase):
    """
        A class for unit-testing function in the clean_tweets_dataframe.py file

        Args:
        -----
            unittest.TestCase this allows the new class to inherit
            from the unittest module
    """

    def setUp(self) -> pd.DataFrame:
        """Dataframe that contains the data from the covid19.json file.
            Returns:
                pd.DataFrame: DF from global_twitter_data.json file.
            """
        self.df = self.df = pd.DataFrame({'created_at': ['2022-08-07 22:31:20+00:00'], 'polarity': ['0.0'],
                                          'retweet_count': ['2'], 'favorite_count': ['1'],'lang': 'de', 'original_text': 'test'},
                                         {'created_at': ['2022-08-07 22:31:16+00:00'], 'polarity': ['1.0'],
                                          'retweet_count': [3], 'favorite_count': [3], 'lang': 'de','original_text': 'test'})

    def test_drop_duplicate(self):
        df = Clean_Tweets(self.df).drop_duplicate(self.df)
        assert df.shape[0] == 1

    def test_convert_to_datetime(self):
        df = Clean_Tweets(self.df).convert_to_datetime(self.df)
        print('working')
        # assert type(df['created_at'][0]) is to_datetime()
        assert type(df['created_at'][0]) is Timestamp

    def test_convert_to_numbers(self):
        df = Clean_Tweets(self.df).convert_to_numbers(self.df)

        assert type(df['polarity'][0]) is numpy.float64 and type(
            df['retweet_count'][0]) is numpy.int64 and type(df['favorite_count'][0]) is numpy.int64

    def test_remove_non_english_tweets(self):
        df = Clean_Tweets(self.df).remove_non_english_tweets(self.df)
        assert df.shape[0] == 0

    if __name__ == '__main__':
        unittest.main()
