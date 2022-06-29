from django.contrib.sitemaps import Sitemap
from .models import *

class Eaish(Sitemap):
    changfreq = 'weekly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Blog.objects.all()
        
    def location(self,obj):
        return '/blog/%s' % (obj.slug)
    
    def lastmod(self, obj):
        return obj.updated_date
        
    
        
    
class EaishPage(Sitemap):
    changfreq = 'weekly'
    priority = 0.9
    protocol = 'http'

    def items(self):
        return Page.objects.all()
        
    def location(self,obj):
        return '/page/%s' % (obj.slug)
    
    def lastmod(self, obj):
        return obj.updated_date
    