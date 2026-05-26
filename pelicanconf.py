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

# --- Dynamic resources filtering for Industry / Solutions pages ---------
# Industry and Solutions pages call get_industry_articles(tag) from their
# resources_section to pull a per-industry list of related blog posts
# instead of hardcoding URLs on every page.
#
# Why an eager scan instead of a Pelican signal: jinja2content renders
# the .md page content as a Jinja2 template at READ time, BEFORE any
# article generator runs. So `signals.article_generator_finalized` fires
# too late — by then the page content is already rendered with empty
# results. Instead we scan content/posts/*.md frontmatter at config
# load time so the cache is ready before jinja2content reads anything.

import os
import re

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_POSTS_DIR = os.path.join(_BASE_DIR, 'content', 'posts')
_META_LINE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$')


def _parse_post_metadata(path):
    """Parse Pelican-style frontmatter from a blog post.

    Returns a dict of lowercased keys → string values, or None when the
    post lacks fields the resources_section needs (image, date) or is a
    draft.
    """
    meta = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    break  # blank line ends frontmatter
                if stripped.startswith('---'):
                    continue  # YAML-style frontmatter delimiter
                m = _META_LINE.match(line.rstrip('\n'))
                if not m:
                    break  # first non-key line ends frontmatter
                meta[m.group(1).lower()] = m.group(2).strip()
    except OSError:
        return None
    if meta.get('status', '').lower() == 'draft':
        return None
    if not meta.get('image'):
        return None
    if not meta.get('date'):
        return None
    if 'slug' not in meta:
        meta['slug'] = os.path.splitext(os.path.basename(path))[0]
    return meta


def _scan_all_posts():
    """Eagerly load all blog posts. Most-recent first."""
    if not os.path.isdir(_POSTS_DIR):
        return []
    posts = []
    for fname in os.listdir(_POSTS_DIR):
        if not fname.endswith('.md'):
            continue
        meta = _parse_post_metadata(os.path.join(_POSTS_DIR, fname))
        if meta:
            posts.append(meta)
    posts.sort(key=lambda m: m.get('date', ''), reverse=True)
    return posts


_posts_cache = _scan_all_posts()


# Categories excluded from the tier-3 (most-recent overall) fallback
# only. Newsletters and Podcasts dominate the recent-post list — they
# would crowd out topical content on every industry page without their
# own tagged coverage. If someone explicitly tags a newsletter or
# podcast post with an industry `tag2`, it still matches at tier 1.
_FALLBACK_EXCLUDED_CATEGORIES = {'newsletter', 'podcast'}


def get_industry_articles(tag, limit=3):
    """Return up to `limit` recent blog posts for an industry tag.

    Three filter tiers, each filling remaining slots without duplicates:

      1. Posts whose `tag2` frontmatter exactly matches `tag`.
      2. Posts whose comma-separated `tags` list contains `tag`
         (case-insensitive substring match).
      3. Most-recent topical posts overall, excluding categories like
         Newsletter and Podcast (see _FALLBACK_EXCLUDED_CATEGORIES).
         Graceful fallback for industries without tagged coverage yet.

    Posts without `image:` or `date:` are skipped during the scan, so
    the resources card never renders a broken image.

    Output shape matches resources_section's `articles` parameter:
        {'url', 'title', 'image_src', 'image_alt'}

    The image_alt falls back to the post title when the post doesn't
    declare an explicit alt — descriptive enough for a featured image.
    """
    seen = set()
    out = []

    def _add(meta):
        url = '/blog/' + meta['slug'] + '/'
        if url in seen:
            return
        seen.add(url)
        out.append({
            'url': url,
            'title': meta.get('title', ''),
            'image_src': meta['image'],
            'image_alt': meta.get('image_alt') or meta.get('title', ''),
        })

    # Tier 1: tag2 exact match.
    for m in _posts_cache:
        if len(out) >= limit:
            break
        if m.get('tag2', '') == tag:
            _add(m)

    # Tier 2: case-insensitive substring of tags.
    if len(out) < limit:
        tag_lower = tag.lower()
        for m in _posts_cache:
            if len(out) >= limit:
                break
            tags = [t.strip().lower() for t in (m.get('tags') or '').split(',')]
            if any(tag_lower in t for t in tags):
                _add(m)

    # Tier 3: most-recent topical fallback (newsletters/podcasts excluded).
    for m in _posts_cache:
        if len(out) >= limit:
            break
        if m.get('category', '').lower() in _FALLBACK_EXCLUDED_CATEGORIES:
            continue
        _add(m)

    return out


# Expose STATS and get_industry_articles to jinja2content so content
# pages can use them. jinja2content renders content files through
# Jinja2 with no context by default; JINJA_GLOBALS is the only way to
# inject names into that environment.
JINJA_GLOBALS = {
    "STATS": STATS,
    "get_industry_articles": get_industry_articles,
}

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