from typing import Protocol
from django.contrib import sitemaps
from django.urls import reverse
from django.conf import settings
from oasis.settings import SITE_ID

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'daily'
    protocol = 'https'
    SITE_ID = 1

    def items(self):
        return ['homepage', 'about', 'services', 'production', 'contact',]

    def location(self, item):
        return reverse(item)