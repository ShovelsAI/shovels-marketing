AUTHOR = 'Shovels'
SITENAME = 'Shovels'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = 'en'
THEME = "themes/shovels"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH_METADATA = '(?P<dirname>.*)/(?P<basename>.*)\..*'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
FILENAME_METADATA = '(?P<title>.*)'

JINJA2CONTENT_TEMPLATES = ['content']
LOAD_CONTENT_CACHE = False

DELETE_OUTPUT_DIRECTORY = True