#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import yaml
from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd()))
from jinja2_utils import resize_image
sys.path.pop(0)


PATH = 'content'
AUTHOR = 'Blind Pandas Team'
SITEURL = 'https://getbookworm.com'
SITENAME = 'Bookworm'
SITESUBTITLE = "The universally accessible document reader"
TIMEZONE = 'Africa/Khartoum'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY  = 'Uncategorised'
RELATIVE_URLS = True
DEVELOPMENT = True
LOAD_CONTENT_CACHE = False
DIRECT_TEMPLATES = ['index',]
JINJA_FILTERS = {'resize_image': resize_image}
# Extra Content info
CONTENT_INFO_FILE = Path(__file__).parent / "content_info.yaml"
with open(CONTENT_INFO_FILE, "r", encoding="utf-8") as file:
    CONTENT_INFO = yaml.safe_load(file)
JINJA_GLOBALS = {
    'site': CONTENT_INFO,
}


# Re-map URLs
ARTICLE_URL = 'blog/post/{slug}/'
ARTICLE_SAVE_AS = 'blog/post/{slug}/index.html'
ARTICLE_LANG_URL = 'blog/post/{lang}/{slug}'
ARTICLE_LANG_SAVE_AS = 'blog/post/{lang}/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}.html'
AUTHOR_SAVE_AS = 'blog/author/{slug}.html'
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS  = '{lang}/{slug}/index.html'

# We don't need to generate the following
DRAFT_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_PAGE_LANG_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Custom theme
THEME  = Path.cwd() / "theme"
THEME_STATIC_DIR = 'theme'

# Static files
STATIC_PATHS = ['static', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'static/*': {'path': 'static/'},
    'static/images/favicon.ico': {'path': 'favicon.ico'},
}

# Plugins
PLUGIN_PATHS = ('plugins',)
PLUGINS = (
    'seo',
    'htmlcompress',
    'readtime',
    'share_post',
    'image_process',
)


# Image Process
IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

# SEO
SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = True
IMAGE_PATH = 'static/images'

# OG properties
OG_LOCALE = "en_US"
HEADER_COVER = "static/images/logo512x512.png"

