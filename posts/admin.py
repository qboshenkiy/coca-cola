from django.contrib import admin
from .models import productViews1, productViews2, news

class ProductViews1Admin(admin.ModelAdmin):
    list_display = ('name', 'info', 'image')

class ProductViews2Admin(admin.ModelAdmin):
    list_display = ('name', 'info', 'image')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

admin.site.register(productViews1, ProductViews1Admin)
admin.site.register(productViews2, ProductViews2Admin)
admin.site.register(news, NewsAdmin)
