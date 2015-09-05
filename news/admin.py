from django.contrib import admin
from models import NewsPost
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(NewsPost, NewsAdmin)