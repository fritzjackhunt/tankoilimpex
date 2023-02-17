from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('production', views.production, name='production'),
    path('contact', views.contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

