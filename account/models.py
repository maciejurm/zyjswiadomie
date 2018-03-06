from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from stream_django.activity import Activity
from stream_django.feed_manager import feed_manager
from django.db.models import signals
from django.db.models.signals import post_delete, post_save
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    biography = models.TextField()
    photo = models.ImageField(upload_to='profile_photo', blank = True)
    facebook = models.URLField()

    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)
