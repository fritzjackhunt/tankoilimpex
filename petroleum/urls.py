from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('production', views.production, name='production'),
    path('contact', views.contact, name='contact'),
]

