from django.db import models

# Create your models here.
class News (models.Model):
    title = models.CharField(max_length=150)
    content = models.TimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatet_add = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_publiched = models.BooleanField(default=True)
