import json
import time
from datetime import datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

# # # # INPUTS # # # # 
fetched_tweets_filename = "tweets.json"
listen_to_userID = ['1059557863775850496'] # reats4charlie user id

# # # # TWITTER UATHENTICATE # # # # 
CONSUMER_KEY = 'mySrItyW5ZySIj1cDaysjMqfv'
CONSUMER_SECRET = 'mm2YClGMdHGxQirnZr3nxGbeGzaJeaLM8lisRc9Tc55gsJZq4o'
ACCESS_TOKEN = '1059557863775850496-Q42lfRBG5SdHzuFCs8bUzJDkD5KOnn'
ACCESS_SECRET = 'T8LCZx7PHsPFJMsmjjE3cn3jGJSwknVUYmouxGdiIIHVy'
#OAuth process, using the keys and tokens
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

# # # # TWITTER AUTHENTICATER # # #
# class TwitterAuthenticator():
#     def authenticate_twitter_app(self):
#         auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#         auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#         return auth

def get_username():
    with open(fetched_tweets_filename, 'r') as rf:
        data = json.load(rf)
    sender_username = '@'+str(data["user"]["screen_name"])
    return sender_username

# # # # TWITTER LISTENER # # # # 
class StdOutListener(StreamListener):
        
    def on_data(self,data):
        print('on_data: Someone tweeted @treats4charlie.')      
        with open(fetched_tweets_filename, 'w') as tf:
            print('Writing tweet to: ' + fetched_tweets_filename)
            tf.write(data)
        with open('debug.json', 'a') as tf:
            print('Writing same tweet to debug.json')
            tf.write(data)
        username = get_username()
        
        # # # CREATE CLIENT TO SEND RESPONSE # # # 
        if username != "@treats4charlie":
            print('senders username: '+ username)
            print('creating TwitterClient: cliente')
            cliente = TwitterClient()
            print('cliente created. sending response tweet...')
            current_time = str(datetime.now())
            message = 'hellooooo '+ username[1:] + ' sent at ' + current_time
            cliente.twitter_client.update_status(str(username) + ' ' + message)
        else:
            print('tweet ignored since it was from charlie')
        return True

    def on_status(self,data):
        return True

    def on_error(self,status):
        print('error: ' + status)

# # # # TWEET READER # # #
    
    # # # # OBTAIN USERNAME OF SENDER # # # 
    # with open(fetched_tweets_filename, 'r') as rf:
    #     data = json.load(rf)
    # sender_username = '@'+str(data["user"]["screen_name"])
    # print(sender_username)

# # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None): #default to none, which will default to my own account
        self.auth = auth
        # self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

if __name__ == '__main__':
    # # # # CREATE LISTENER OBJECT # # # 
    listener = StdOutListener()
    stream = Stream(auth,listener)
    stream.filter(follow=listen_to_userID)
    # #send response tweet
    # message = 'hellooooo auto response from python!'
    # # username = '@cvaldez83'
    # print('creating cliente')
    # cliente = TwitterClient()
    # print('sending response tweet')
    # cliente.twitter_client.update_status(str(get_username()) + ' ' + message)
    # print(get_username())