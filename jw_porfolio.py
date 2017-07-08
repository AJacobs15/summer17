import tweepy



#make sure to copy and past in access keys
consumer_key = 'gO8Zg0I7Q7LRyokzoqRMza3sF'
consumer_secret='8XYuVlcLSmk1T5pzIclRLrRA8GYPVR9vtjWlJNkOVipAgRJ8O9'
access_token_key='823349131464818689-JhZCJ6VEroPLSkUAeO9gOBoAv3XpaRe'
access_token_secret = '0hTFQcS9BXGRdAWVZkvdnPRR3AnxbF8H5uheFARcJJQqV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


search_hashtag = tweepy.Cursor(api.search, q='aapl').items(1000)


count = 0
for term in search_hashtag:
    count += 1

print(count)


