import pandas as pd
import tweepy as tw
import time

#Define credentials
consumer_key =  'consumer_key'
consumer_secret = 'consumer_Secret'
access_key = 'access_key'
access_secret = 'access_secret'

#create access token
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth)

#Set keyword search & date
keyword = 'covid'+ " -filter:retweets"
search_date = '2020-03-01'

#Define function for downloading tweets
def search_tweet(search_term, date_search, max_id_str):
    tweets = tw.Cursor(api.search,
                       q=keyword,
                       lang="en",
                       since=search_date,
                       max_id=max_id_str).items(150)
    res = [[tweet.user.screen_name, tweet.user.location, tweet.text, tweet.created_at, tweet.id] for tweet in tweets]
    res_df = pd.DataFrame(data=res, columns=["user", "location", "text", "time_creation", "id"])
    return res_df

#extract the tweets & save them in a data frame
max_id = -1
all_tweets = pd.DataFrame(columns=["user", "location", "text", "time_creation", "id"])
for i in range(0, 50):
    try:
        res = search_tweet(keyword, search_date, max_id)
        all_tweets = all_tweets.append(res)
        max_id = (res['id'].iloc[-1]) - 1
    except BaseException as e:
        print("Failed", str(e))
        time.sleep(10)

#Save data frames
all_tweets.to_csv('tweets2.csv')