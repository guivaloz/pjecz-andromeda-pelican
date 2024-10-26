"""
Configuration file for Pelican
"""

# Author, sitename, and siteurl
AUTHOR = "PJECZ Direccion de Informatica"
SITENAME = "Justicia Digital"
SITEDESCRIPTION = "Plataformas del Poder Judicial del Estado de Coahuila de Zaragoza"
SITEURL = ""
SITELOGO = "theme/images/icon-normal.png"

# Content path
PATH = "content"

# Categories titles
CATEGORIES_TITLES = {"blog": "Blog"}

# Article paths
ARTICLE_PATHS = ["blog"]

# Pages paths
PAGE_PATHS = ["pages", "plataformas"]

# Static paths and files
STATIC_PATHS = ["plataformas", "favicon.ico", "robots.txt"]

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = False

# Los artículos van en directorios por categoria/titulo/
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = "{category}/{slug}/"
PAGE_SAVE_AS = "{category}/{slug}/index.html"

# Theme
THEME = "themes/justiciadigital"

# Timezone and language
TIMEZONE = "America/Monterrey"
DEFAULT_LANG = "es"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Pagination is off
DEFAULT_PAGINATION = False

# Use relative URLs
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican_javascript", "sitemap"]

# Plugin sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "indexes": 0.5,
        "pages": 1,
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "weekly",
    },
    "exclude": [
        "archives.html",
        "categories.html",
        "tags.html",
        "author/",
        "category/",
        "tag/",
    ],
}
