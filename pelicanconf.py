#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anthony Roy'
SITENAME = u'Anthony Roy'
SITEURL = ''

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
SOCIAL = (('@antroy at GitHub', 'https://github.com/antroy'),
         )

DEFAULT_PAGINATION = False
DISQUS_SITENAME = "Velocity"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
