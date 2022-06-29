from django.urls import path
from home import views
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .sitemap import *

sitemaps = {
    'blog':Eaish,
    'page':EaishPage,
}

app_name = "Eaish"

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/<slug>',views.blog,name='blog'),
    path('page/<slug>',views.page,name='page'),
    path('s',views.search,name='search'),
    path("robots.txt",TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),
    path("manifest.json",TemplateView.as_view(template_name="main/manifest.json", content_type="text/plain")),
    path("ads.txt",TemplateView.as_view(template_name="main/ads.txt", content_type="text/plain")),
    path('category/<category>',views.category,name='category'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

