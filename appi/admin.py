from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'date_creation')
    search_fields = ('titre',)

admin.site.register(Article, ArticleAdmin)
