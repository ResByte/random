import tweepy
from tweepy.streaming import StreamListener

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


consumer_key = '#Enter your key'
consumer_secret = '#Enter your consumer secret'
access_token = '# Enter access token'
access_token_secret = '# Enter access token secret'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

l = StdOutListener()
stream = tweepy.Stream(auth,l)
stream.filter(track=['Apple', 'Samsung'])
