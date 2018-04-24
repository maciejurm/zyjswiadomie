from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Video(models.Model):
    title = models.CharField(max_length=250, verbose_name='Tytuł')
    video_url = models.CharField(max_length=255, verbose_name = 'Link do filmu')
    image = models.ImageField(upload_to = 'video', verbose_name='Miniatura filmu')
    body = models.TextField(verbose_name='Opis filmu')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length= 250)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('video:video_detail',
                      args = [
                          self.slug
                      ])
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Video.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
