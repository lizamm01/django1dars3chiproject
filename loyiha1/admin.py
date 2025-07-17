from django.contrib import admin
from .models import *

class MahallaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('title', 'created_at')
    search_fields = ['title']
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_bool')
    list_editable = ['is_bool']

class TumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('title', 'created_at')
    search_fields = ['title']
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_bool')
    list_editable = ['is_bool']

class ViloyatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('title', 'created_at')
    search_fields = ['title']
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_bool')
    list_editable = ['is_bool']

admin.site.register(Mahalla, MahallaAdmin)
admin.site.register(Tuman, TumanAdmin)
admin.site.register(Viloyat, ViloyatAdmin)
