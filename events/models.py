from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Tytuł')
    image = models.ImageField(upload_to = 'events', verbose_name='Miniatura wydarzenia')
    body = models.TextField(verbose_name='Treść')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    day = models.DateField('Dzień wydarzenia', help_text = 'Dzień wydarzenia')
    start_time = models.TimeField('Godzina rozpoczęcia', help_text = 'Godzina rozpoczęcia')
    end_time = models.TimeField('Zakończenie')
    active = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Wydarzenie'
        verbose_name_plural = 'Wydarzenia'
    
    def get_absolute_url(self):
        return reverse('event:event_detail',
                      args = [
                          self.slug
                      ])
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
