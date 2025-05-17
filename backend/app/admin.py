from django.contrib import admin
from .models import ShortenedURL

@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'clicks', 'created_at')
    search_fields = ('original_url', 'short_code')
    readonly_fields = ('short_code', 'clicks', 'created_at')
