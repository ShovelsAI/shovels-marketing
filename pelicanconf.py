AUTHOR = 'Shovels'
SITENAME = 'Shovels | '
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False

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
STATIC_PATHS = ['images', 'pages', 'extras', 'pdfs']

# Copy favicon files to site root for browser/crawler compatibility
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/install.sh': {'path': 'install.sh'},
}

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

# Plugins
PLUGINS = ['jinja2content', 'sitemap']

# Canonical stats — update this dict when numbers change.
# Templates and content pages reference these via {{ STATS.key }}.
# Mirror updates to the snippets/stats.mdx file in the docs repo.
STATS = {
    # Homepage / widely published stats
    "permits": "130M+",
    "contractors": "2.3M+",
    "jurisdictions": "1,800+",
    "monthly_permits": "5M+",

    # Permit breakdowns
    "permits_residential": "69M+",
    "permits_commercial": "16M+",
    "permits_residential_commercial": "84M+",

    # Data feed table counts
    "residents": "46M+",
    "homeowners": "24M+",
    "addresses": "23M+",
    "parcels": "160M+",
}

# Expose STATS to jinja2content so content pages can use {{ STATS.key }}.
# jinja2content renders content files through Jinja2 with no context by default;
# JINJA_GLOBALS is the only way to inject variables into that environment.
JINJA_GLOBALS = {"STATS": STATS}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}