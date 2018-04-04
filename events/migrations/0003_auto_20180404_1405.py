# Generated by Django 2.0.2 on 2018-04-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, verbose_name='Godzina zakończenia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, help_text='Godzina rozpoczęcia', verbose_name='Godzina rozpoczęcia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='video_url',
            field=models.URLField(blank=True, help_text='Jeśli masz zapowiedź wydarzenia w formie wideo, możesz tutaj wstawić. Jeśli prowadzisz live na facebooku, wstaw do niego link, a osoby zainteresowane będą mogły kliknąć "Otrzymaj powiadomienie" bezpośrednio z Żyj świadomie.', verbose_name='Link do wideo'),
        ),
    ]
