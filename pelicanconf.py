#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican.readers import *

AUTHOR = u'Anthony Roy'
SITENAME = u'Anthony Roy'
SITEURL = 'http://antroy.github.io'

THEME = './theme/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'
ARTICLE_DIR = './content'

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
PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}
READERS = {'rest': RstReader, 'rest.txt': RstReader}
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
