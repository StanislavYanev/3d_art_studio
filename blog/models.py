from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language

class Article(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    content_en = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def translated_title(self):
        if get_language() == 'en' and self.title_en:
            return self.title_en
        return self.title

    def translated_content(self):
        if get_language() == 'en' and self.content_en:
            return self.content_en
        return self.content
    
    def __str__(self):
        return self.title
