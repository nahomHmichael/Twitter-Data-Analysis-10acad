import pandas as pd


class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')

    def drop_unwanted_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count'].index
        df.drop(unwanted_rows, inplace=True)
        df = df[df['polarity'] != 'polarity']
        #print(df.head())

        return df

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """

        df = df.drop_duplicates()
        #print(df.head(2))

        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(self.df['created_at'], errors='coerce')   # coeerce argument to set invalid parsing as NaT

        self.df = self.df[self.df['created_at'] >= '2020-12-31']
        #print(self.df.head(2))

        return self.df

    def convert_to_numbers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df['polarity'] = pd.to_numeric(self.df['polarity'], errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(self.df['retweet_count'], errors='coerce')
        self.df['favorite_count'] = pd.to_numeric(self.df['favorite_count'], errors='coerce')
        #print(self.df['polarity'].head())
        return self.df

    def remove_non_english_tweets(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove non english tweets from lang
        """

        self.df = df[df['lang']=='en']
        #print(self.df['lang'].head())
        return self.df


if __name__ == "__main__":
    processed_df = pd.read_csv('processed_tweet_data.csv')
    cleaner = Clean_Tweets(df=processed_df)
    processed_df = cleaner.drop_unwanted_column(processed_df)
    processed_df = cleaner.drop_duplicate(processed_df)
    processed_df = cleaner.convert_to_datetime(processed_df)
    processed_df = cleaner.convert_to_numbers(processed_df)
    processed_df = cleaner.remove_non_english_tweets(processed_df)

    processed_df.to_csv('clean_processed_tweet_data.csv')
    print('processed tweet cleaned!')
    print('File Saved Successfully!!!')
