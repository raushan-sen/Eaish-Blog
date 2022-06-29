from django.contrib import admin
from .models import *

admin.site.register(Categery)

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    class Media:
        js= ('js/main.js',)

@admin.register(Seo_Setup)
class Seo_Setupadmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

@admin.register(Page)
class Pageadmin(admin.ModelAdmin):
    class Media:
        js= ('js/main.js',)