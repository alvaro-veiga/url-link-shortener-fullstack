from django.db import models
import random
import string

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        length = 6
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            if not ShortenedURL.objects.filter(short_code=code).exists():
                return code

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"
