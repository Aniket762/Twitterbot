#using twitter api
import tweepy
import time

auth = tweepy.OAuthHandler('WMfVJfOA6eBlaoLPkOTfDXdhL','a63Dqba8R7lfDsQtkrcwTPIV90qLVHQgsmaMnod16uFeeOcGcD')
auth.set_access_token('1288198847101980672-SCmkp3KdhF8hf9aLSwnxoL6VQ4Adeu','V6hZ9td82HUdVlZwJzaiwwFe7oPLQkfPSvu8vGwZGJ1wV')
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


user = api.me()
print(user)

search = 'Hackathons'
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

'''
    this is for liking the tweets


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