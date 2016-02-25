#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican.readers import *
import sys, os

AUTHOR = u'Anthony Roy'
SITENAME = u'Anthony Roy'
SITEURL = 'https://antroy.github.io'

THEME = './theme/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'
ARTICLE_PATHS = ['./content']

MENUITEMS = (('Tags', 'tags.html'),)

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('xkcd', 'http://xkcd.org/'),
          ('The System', 'http://www.systemcomic.com/'),
         )

# Social widget
SOCIAL = (
        ('@antroy at GitHub', 'https://github.com/antroy'),
        ('@antroy at Twitter', 'https://twitter.com/antroy'),
         )

DEFAULT_PAGINATION = False
DISQUS_SITENAME = "antroy"

ADDTHIS_PROFILE = 'ra-52f76e637a77ab77'

PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}
READERS = {'rest': RstReader, 'rest.txt': RstReader}

RELATIVE_URLS = True if os.environ.has_key("ENV") and os.environ["ENV"] == "dev" else False

if RELATIVE_URLS:
    print "Using relative URLS for links"

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['neighbors']
