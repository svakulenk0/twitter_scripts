#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
28 November 2017
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

'''
from twython import Twython, TwythonRateLimitError

from twitter_settings import *

ISWC_PAPER_URLS = "iswc2017.semanticweb.org/paper"


def search(keyword):
    twitter = Twython(APP_KEY, APP_SECRET,
                       OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    # result = twitter.search(q=keyword)
    # print str(result['search_metadata']['count']) + ' tweets'
    # print result

    results = twitter.cursor(twitter.search, q=keyword)
    for result in results:
        print(result)


if __name__ == '__main__':
    search(keyword=ISWC_PAPER_URLS)
