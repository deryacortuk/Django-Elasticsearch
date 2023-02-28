from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","published_time"]
    list_display_links = ["title", "author", "published_time"]
    class Meta:
        model = Article
        fields = ["title", "author","published_time"]


