from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Webinar(models.Model):
    title = models.CharField(max_length = 255)
    webinar = EmbedVideoField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'webinars')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, default='test')

    class Meta:
        verbose_name = 'Webinar'
        verbose_name_plural = 'Webinary'
    