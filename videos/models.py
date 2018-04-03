from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Video(models.Model):
    title = models.CharField(max_length=250, verbose_name='Tytuł')
    video_url = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'video', verbose_name='Miniatura filmu')
    body = models.TextField(verbose_name='Opis filmu')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'
    
    def get_absolute_url(self):
        return reverse('video:video_detail',
                      args = [
                          self.slug
                      ])