from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'
        ordering = ('created_at',)

    def __str__(self):
        self.name
