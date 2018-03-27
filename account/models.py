from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    biography = models.TextField()
    photo = models.ImageField(upload_to='profile_photo', blank = True)
    facebook = models.URLField()

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)