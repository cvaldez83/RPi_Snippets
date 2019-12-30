#!/usr/bin/env python

#command prompt:
#python nudge.py handles.txt "your message"
from tweepy import API
import tweepy, sys, time
from random import randint
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#api = tweepy.API(auth) #import tweepy
api = API(auth) #from tweepy import API

filename = 'charliedetected.mp4'
upload_result = api.media_upload(filename)
message = 'sending from python'
 
handles = sys.argv[1]
f = open(handles, "r")
h = f.readlines()
f.close()
 
for i in h:
    i = i.rstrip()
    m = i + " " + sys.argv[2]
    print(m)
    #s = api.update_status(m)
    #s = api.update_with_media(filename, status=message)
    s = api.update_status(status=message, media_ids=[upload_result.media_id_string])
    nap = randint(1, 2)
    time.sleep(nap)