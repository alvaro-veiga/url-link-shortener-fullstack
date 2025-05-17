from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_code', 'short_url', 'clicks', 'created_at']
        read_only_fields = ['short_code', 'clicks', 'created_at']

    def get_short_url(self, obj):
        request = self.context.get('request')
        if request:
            return f"{request.scheme}://{request.get_host()}/{obj.short_code}"
        return None 