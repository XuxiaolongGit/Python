from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'column',
        'modified_time',
    ]
    exclude = ['author']
    search_fields = ['title','column']
    list_filter = ['column']
