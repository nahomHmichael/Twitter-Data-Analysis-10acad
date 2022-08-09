import json
import pandas as pd
from textblob import TextBlob
import re


def read_json(json_file: str) -> list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """

    tweets_data = []
    for tweets in open(json_file, 'r'):
        tweets_data.append(json.loads(tweets))

    return len(tweets_data), tweets_data


class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """

    def __init__(self, tweets_list):

        self.tweets_list = tweets_list

    # an example function
    def find_statuses_count(self) -> list:
        """
        A function to extract the status count

        Returns:
            list: statuses_count

        """
        statuses_count = []
        for count in self.tweets_list:
            statuses_count.append(count['user']['statuses_count'])
        return statuses_count

    def find_full_text(self) -> list:
        """
        A function to extract tweet text.

        Returns:
            List: original tweet text and clean tweet text

        """
        original_text = []
        tidy_text = []

        for text in range(len(self.tweets_list)):
            original_text.append((self.tweets_list[text]['full_text']))
            tidy_text.append(re.sub("^RT.*:", "", self.tweets_list[text]['full_text']))

        return original_text, tidy_text

    def find_sentiments(self, text) -> list:
        """
        A function to extract sentiment from text using textblob for natural languange processing.

        Args:
            text:

        Returns:
            list: polarity and subjectivity

        """
        polarity = []
        subjectivity = []
        for tweet in text:
            tweet_sentiment = TextBlob(tweet).sentiment
            polarity.append(tweet_sentiment.polarity)
            subjectivity.append(tweet_sentiment.subjectivity)

        return polarity, subjectivity

    def find_created_time(self) -> list:
        """
        A function that extracts the dates which the tweets got tweeted.

        Returns:
            list: created_at

        """
        created_at = []

        for time in range(len(self.tweets_list)):
            created_at.append((self.tweets_list[time]['created_at']))

        return created_at

    def find_source(self) -> list:
        """
        A function that extracts the hyperlink source of the tweets.

        Returns:
            list: source

        """
        source = []
        for s in range(len(self.tweets_list)):
            source.append((self.tweets_list[s]['source']))

        return source

    def find_screen_name(self) -> list:
        """

        Returns:

        """
        screen_name = []
        for usr in range(len(self.tweets_list)):
            screen_name.append(self.tweets_list[usr]['user']['screen_name'])

        return screen_name

    def find_followers_count(self) -> list:
        """

        Returns:

        """
        followers_count = []
        for follower in range(len(self.tweets_list)):
            followers_count.append(self.tweets_list[follower]['user']['followers_count'])

        return followers_count

    def find_friends_count(self) -> list:
        friends_count = []
        for friends in range(len(self.tweets_list)):
            friends_count.append(self.tweets_list[friends]['user']['friends_count'])

        return friends_count

    def is_sensitive(self) -> list:
        is_sensitive = [x.get('possibly_sensitive', None) for x in self.tweets_list]

        return is_sensitive

    def find_favourite_count(self) -> list:
        favourite_count = []
        for likes in range(len(self.tweets_list)):
            favourite_count.append(self.tweets_list[likes]['user']['favourites_count'])

        return favourite_count

    def find_retweet_count(self) -> list:
        retweet_count = []
        for rt in range(len(self.tweets_list)):
            retweet_count.append(self.tweets_list[rt]['retweet_count'])

        return retweet_count

    def find_hashtags(self) -> list:
        hashtags = []
        for hstg in range(len(self.tweets_list)):
            hashtags.append(self.tweets_list[hstg]['entities']['hashtags'])

        return hashtags

    def find_mentions(self) -> list:
        mentions = [x.get('user_mentions', None) for x in self.tweets_list]

        return mentions

    def find_location(self) -> list:
        location = [x['user']['location'] for x in self.tweets_list]

        return location

    def find_lang(self) -> list:
        lang = []
        for lg in range(len(self.tweets_list)):
            lang.append((self.tweets_list[lg]['lang']))

        return lang

    def find_coordinates(self) -> list:
        coordinates = []
        for coord in range(len(self.tweets_list)):
            coordinates.append(self.tweets_list[coord]['coordinates'])

        return coordinates

    def find_screen_count(self) -> list:
        screen_count = []
        for count in range(len(self.tweets_list)):
            screen_count.append(self.tweets_list[count]['user']['listed_count'])

        return  screen_count

    def find_sentiment(self, polarity, subjectivity) -> list:
        sentiment = []
        for i in range(len(polarity)):
            if polarity[i] > 0:
                sentiment.append(1)
            elif polarity[i] < 0:
                sentiment.append(0)
            else:
                sentiment.append(-1)

        return sentiment

    def get_tweet_df(self, save=False) -> pd.DataFrame:
        """required column to be generated you should be creative and add more features"""

        columns = ['created_at', 'statuses_count', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang', 'favorite_count',
                   'retweet_count',
                   'original_author', 'screen_count', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags',
                   'user_mentions', 'place', 'place_coord_boundaries']

        statuses_count = self.find_statuses_count()
        created_at = self.find_created_time()
        source = self.find_source()
        text, clean_text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(clean_text)
        sentiment = self.find_sentiment(polarity, subjectivity)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()
        coordinates = self.find_coordinates()
        screen_count = self.find_screen_count()

        data = zip(created_at, statuses_count, source, text, clean_text, sentiment, polarity, subjectivity, lang, fav_count, retweet_count, screen_name, screen_count,
                   follower_count, friends_count, sensitivity, hashtags, mentions, location, coordinates)
        df = pd.DataFrame(data=data, columns=columns)
        print(polarity[0:5])

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')

        return df


if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'statuses_count', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang',
               'favorite_count', 'retweet_count',
               'original_author', 'screen_count', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags',
               'user_mentions', 'place', 'place_coord_boundaries']

    _, tweet_list = read_json("./data/global_twitter_data.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df(save=True)

    # use all defined functions to generate a dataframe with the specified columns above
