# Generated by Django 2.0.2 on 2018-04-23 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Tytuł')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField(help_text='Aby inaczej sformatować tekst, zaznacz fragment tekstu, który chcesz zmienić i kliknij wybraną ikonę.', verbose_name='Treść')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, help_text='Aby nie łamać praw autorskich, warto skorzystać z darmowych zdjęć na stocksnap.io, unsplash.com lub pexels.com. Warto jednak pamiętać o rozdzielczości', upload_to='post_image', verbose_name='Miniatura postu')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
