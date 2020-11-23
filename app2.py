#using twitter api
import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.access_token('','')
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


user = api.me()
print(user)

search = ''
nrTweets = 500

# for liking tweets
'''
for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


    this is for liking the tweets
'''

# for retweeting
for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
