import os
import sys
import unittest

import numpy
import pandas as pd
from clean_tweets_dataframe import Clean_Tweets
from pandas._libs.tslibs.timestamps import Timestamp

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
                pd.DataFrame: DF from Economic_Twitter_data.json file.
            """
            self.df = self.df = pd.DataFrame({'created_at': [
                '2022-08-07 22:31:20+00:00'], 'polarity': ['0.0'], 'retweet_count': ['2'], 'favorite_count': ['1.0'],
                'lang': 'de', 'original_text': 'test'}, {'created_at': [
                '6/2/2022 10:25'], 'polarity': ['1.0'], 'retweet_count': [3.0], 'favorite_count': [3.0], 'lang': 'de',
                'original_text': 'test'})


    if __name__ == '__main__':
        unittest.main()

