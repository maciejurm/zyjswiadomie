# Generated by Django 2.0.2 on 2018-04-03 21:41

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
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Tytuł')),
                ('video_url', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='video', verbose_name='Miniatura filmu')),
                ('body', models.TextField(verbose_name='Opis filmu')),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmy',
            },
        ),
    ]
