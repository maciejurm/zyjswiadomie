from django.db import models
from django.contrib.auth.models import User
from stream_django.activity import Activity
from django.urls import reverse

class Post(models.Model, Activity):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(unique = True)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = False)
    image = models.ImageField(upload_to = 'post_image', blank = True)
    

    @property
    def activity_actor_attr(self):
        return self.author

    class Meta:
        ordering = ['-created_at']

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