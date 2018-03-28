from django.db import models
from django.contrib.auth.models import User

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