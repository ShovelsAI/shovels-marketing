AUTHOR = 'Shovels'
SITENAME = 'Shovels | '
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

USE_FOLDER_AS_CATEGORY = True
ARTICLE_PATHS = ['posts']
ARTICLE_EXCLUDES = ['pages']
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'date'
SLUGIFY_SOURCE = 'title'
ARCHIVES_SAVE_AS = 'blog/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'
DRAFT_URL = 'blog/drafts/{slug}/'
DRAFT_SAVE_AS = 'blog/drafts/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/','{base_name}/{number}/index.html'),
)
FORMATTED_FIELDS = ['summary', 'title']
STATIC_PATHS = ['images', 'pages']

# Theme static files configuration
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

PATH_METADATA = r'(?P<dirname>.*)/(?P<basename>.*)\..*'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
FILENAME_METADATA = '(?P<title>.*)'

JINJA2CONTENT_TEMPLATES = ['content']
LOAD_CONTENT_CACHE = False

# 404 page configuration
ERROR_404_SAVE_AS = '404.html'
ERROR_404_URL = '404.html'

DELETE_OUTPUT_DIRECTORY = True