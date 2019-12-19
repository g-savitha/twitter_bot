import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key' , 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()
# print(user.followers_count)
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

#narciscist bot - loves tweets based on key words and retweets the tweets
search_string = '100 days of code'
number_of_tweets = 2

for  tweet in tweepy.Cursor(api.search,search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        tweet.retweet()
        print('Liked a tweet!')
    except tweepy.TweepError as e:
        print(e.reason())
    except StopIteration:
        break

# generous bot - follow a particular person from followers list.
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if(follower.name == 'React India'):
        follower.follow()
        break
