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

class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name = 'follow', on_delete = models.CASCADE)
    target = models.ForeignKey('auth.User', related_name ='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user', 'target')

def unfollow_feed(sender, instance, **kwargs):
    feed_manager.unfollow_user(instance.user_id, instance.target_id)

def follow_feed(sender, instance, **kwargs):
    feed_manager.follow_user(instance.user_id, instance.target_id)

signals.post_delete.connect(unfollow_feed, sender=Follow)
signals.post_save.connect(follow_feed, sender=Follow)