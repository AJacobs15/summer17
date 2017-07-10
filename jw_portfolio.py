import tweepy
from textblob import TextBlob
import time
import pandas as pd

#make sure to copy and past in access keys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


start_time = time.time()
search_hashtag = tweepy.Cursor(api.search, q='aapl').items(2000)
end_time = time.time()

print(end_time - start_time)




def classify_sentiment(search):
    '''
    Inpupt: search is the rv of a tweepy.Cursor call
    Returns: summary statistics of the tweets


    maybe also grab data on location of tweet?
    '''
    polarity_list = []
    objectivity_list = []
    text_list = []
    coordinate_list = []
    geo_list = []

    counter = 0
    for term in search:
        counter += 1
        
        print(counter)
        text = term.text
        coordinate = term.coordinates
        geo = term.geo

        text_blob = TextBlob(text)
        sentiment = text_blob.sentiment
        polarity = sentiment[0]
        objectivity = sentiment[1]
        
        polarity_list.append(polarity)
        objectivity_list.append(objectivity)
        text_list.append(text)
        coordinate_list.append(coordinate)
        geo_list.append(geo)

    d = {'polarity' : polarity_list, 'objectivity': objectivity_list, 
            'text' : text_list, 'coordinates': coordinate_list, 
            'geo': geo_list}
    df = pd.DataFrame.from_dict(d)
    return df

