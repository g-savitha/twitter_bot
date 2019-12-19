import tweepy
import time

auth = tweepy.OAuthHandler('32QovOsEq8xHzv8vm90FoOzdK' , 'FX6INoxWWaN6gqNZmXym3UeCPz70jMK4H51SIyTAAUtrtkvtuk')
auth.set_access_token('252473758-kIlDhtSz0pZ1Tv2jEjuEnsO9vZWjlY8aWMygSAhW', '8V7lhBR4TevZCMQG7mI6q9YJaWJCcMKYcBXiMoXAQypww')

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