#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chris Jefferson'
SITENAME = u'Six Months To Fitness (and beyond)'
SITEURL = 'http://fitness.azumanga.org'

DISQUS_SITENAME=u'azumanga'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

FEED_DOMAIN = SITEURL
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_AD_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Azumanga'),
          ('Facebook', 'https://www.facebook.com/azumanga'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="/Users/caj/progs/pelican-themes/blueidea"