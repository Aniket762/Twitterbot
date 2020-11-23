#using twitter api
import tweepy
import time

auth = tweepy.OAuthHandler('WMfVJfOA6eBlaoLPkOTfDXdhL','a63Dqba8R7lfDsQtkrcwTPIV90qLVHQgsmaMnod16uFeeOcGcD')
auth.set_access_token('1288198847101980672-v5pLMnapQbwsduoD6SnteuQhh1eWws','fmC3txEy1ShxAozphVx7UPZiwydFh4UJ4Ukhckid7dJWM')
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


user = api.me()
print(user)

search = ''
nrTweets = 500

# for liking tweets

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
'''