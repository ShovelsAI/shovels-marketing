# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

CANONICAL_SITEURL = 'https://www.shovels.ai'

# Absolute URLs are baked in at build time, so a preview deployment built
# against the canonical domain links away from the very build being reviewed.
# Preview builds therefore use the domain they are served from. SITEURL in the
# environment overrides both, and production builds keep the canonical domain.
SITEURL = os.environ.get('SITEURL')
if not SITEURL:
    preview_host = os.environ.get('VERCEL_URL') or os.environ.get('VERCEL_BRANCH_URL')
    if os.environ.get('VERCEL_ENV') in ('preview', 'development') and preview_host:
        SITEURL = 'https://' + preview_host
    else:
        SITEURL = CANONICAL_SITEURL

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'docs'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""