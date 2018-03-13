from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from meta.models import ModelMeta


class Post(ModelMeta, models.Model):
    title = models.CharField(max_length = 250, verbose_name='Tytuł')
    slug = models.SlugField(unique = True)
    body = models.TextField(verbose_name='Treść', help_text='Aby inaczej sformatować tekst, zaznacz fragment tekstu, który chcesz zmienić i kliknij wybraną ikonę.')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'post_image', blank = True, verbose_name='Miniatura postu', help_text='Aby nie łamać praw autorskich, warto skorzystać z darmowych zdjęć na stocksnap.io, unsplash.com lub pexels.com. Warto jednak pamiętać o rozdzielczości')

    class Meta:
        ordering = ['-created_at']

    _metadata = {
        'title': 'title',
        'description': 'body',
        'image': 'get_meta_image'
    }

    def get_meta_image(self):
        if self.image:
            return self.image.url

    def get_absolute_url(self):
        return reverse('blog:tresc_postu',
                      args = [
                          self.slug
                      ])
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Treść')
    created_at = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'
        ordering = ('created_at',)

    def __str__(self):
        return 'Komentarz dodany przez {} dla posta {}'.format(self.name, self.post)
