from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length = 250, verbose_name = 'Tytuł')
    image = models.ImageField(upload_to = 'events', verbose_name='Miniatura wydarzenia')
    video_url = models.URLField(blank=True,verbose_name='Link do wideo', help_text='Jeśli masz zapowiedź wydarzenia w formie wideo, możesz tutaj wstawić. Jeśli prowadzisz live na facebooku, wstaw do niego link, a osoby zainteresowane będą mogły kliknąć "Otrzymaj powiadomienie" bezpośrednio z Żyj świadomie.')
    button = models.CharField(max_length = 100, default = 'Więcej informacji', verbose_name = 'Przycisk', help_text = 'Możesz zmienić nazwę przycisku wpisując na przykład: "Bilety"')
    button_url = models.URLField(default = 'http://przykladowylink.pl', verbose_name='Adres url przycisku', help_text = 'Przekierowanie przycisku na podany adres, tutaj wpisz adres na który chcesz skierować ludzi zainteresowanych wydarzeniem.')
    body = models.TextField(verbose_name='Treść')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length= 250)
    day = models.DateField('Dzień wydarzenia', help_text = 'Dzień wydarzenia')
    start_time = models.TimeField('Godzina rozpoczęcia', help_text = 'Godzina rozpoczęcia', blank=True)
    end_time = models.TimeField('Godzina zakończenia', blank=True)
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
