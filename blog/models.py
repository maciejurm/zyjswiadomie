from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



class Post(models.Model):
    title = models.CharField(max_length = 250, verbose_name='Tytuł')
    slug = models.SlugField(unique = True, max_length= 250)
    body = models.TextField(verbose_name='Treść', help_text='Aby inaczej sformatować tekst, zaznacz fragment tekstu, który chcesz zmienić i kliknij wybraną ikonę.')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'post_image', blank = True, verbose_name='Miniatura postu', help_text='Aby nie łamać praw autorskich, warto skorzystać z darmowych zdjęć na stocksnap.io, unsplash.com lub pexels.com. Warto jednak pamiętać o rozdzielczości')

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('blog:tresc_postu',
                      args = [
                          self.slug
                      ])
    
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    
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
