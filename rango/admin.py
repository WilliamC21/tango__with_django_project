from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from rango.models import Category, Page

class PageAdmin (admin.ModelAdmin):
    list_display = ('title','category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)


