from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published =models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at'] # newest posts first
        