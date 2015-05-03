#!/usr/bin/env python
# Common settings

AUTHOR = u'Chris Jefferson'

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

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Azumanga'),
          ('Facebook', 'https://www.facebook.com/azumanga'),
          ('github', 'https://github.com/ChrisJefferson'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="pelican-bootstrap3"

BOOTSTRAP_THEME = "yeti"

STATIC_PATHS = ['images','generic-static']

CUSTOM_CSS = 'generic-static/css/custom.css'