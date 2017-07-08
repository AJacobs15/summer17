import tweepy




consumer_key = 'KBwykgDKssvUi6a9g6AQouekf'
consumer_secret='0J5hxQubZpq1D9oFGgKlF8nmejhlziYfnToOqzZI0iDKKKn8Wp'
access_token_key='150235316-ACR5oR7s44sAuDokXNwZ8K8c4H4bSNwp5Exy1kvt'
access_token_secret = 'zOGtr4iEAdbvfC2C3i3lakd2inx3UCI4COm1qaSyOwFdK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)



)

'''

search_hashtag = tweepy.Cursor(api.search, q='aapl').items(1000)


public_tweets = api.home_timeline()
'''
for tweet in public_tweets:
	print (tweet.text)
'''
user = api.get_user('twitter')
print(user.screen_name)
print(user.followers_count)
friends = user.friends()
	print (tweet.text)'''
"""
search = api.GetSearch(term = "#aapl")

print(search[1].text)


def test():
    '''
    I'm just playing around here. 
    '''
    search = api.GetSearch(term = "#aapl", count = 100)


    count = 0
    for term in search:
        count += 1
        print(term.text)
        print()
        print()

    print(count)

"""