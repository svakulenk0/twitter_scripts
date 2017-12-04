#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
4 December 2017
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

'''
from tweepy.streaming import StreamListener
from tweepy import Stream, OAuthHandler

from twitter_settings import *


class MyStreamListener(StreamListener):
    '''
    Overrides Tweepy class for Twitter Streaming API
    '''

    def on_status(self, status):
        # ignore retweets
        if not hasattr(status,'retweeted_status') and status.in_reply_to_status_id == None:
            tweet_text = status.text
            print(tweet_text)
            # store tweets to Mongo
            # store_tweet(tweet_id, tweet_text)

    def on_error(self, status_code):
        print (status_code, 'error code')


def stream_tweets(keywords=['python']):
    '''
    Connect to Twitter API and fetch relevant tweets from the stream
    '''
    listener = MyStreamListener()
    auth_handler = OAuthHandler(APP_KEY, APP_SECRET)
    auth_handler.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    # start streaming
    while True:
        try:
            stream = Stream(auth_handler, listener)
            print ('Listening...')
            stream.filter(track=keywords)
        except Exception as e:
            # reconnect on exceptions
            print (e)
            continue


if __name__ == '__main__':
    stream_tweets()
