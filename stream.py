#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
4 December 2017
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

'''

from twython import TwythonStreamer

from twitter_settings import *


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)


stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.sample()
