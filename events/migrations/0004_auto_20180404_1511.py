# Generated by Django 2.0.2 on 2018-04-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180404_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Godzina zakończenia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, help_text='Godzina rozpoczęcia', null=True, verbose_name='Godzina rozpoczęcia'),
        ),
        migrations.AlterField(
            model_name='event',
            name='video_url',
            field=models.URLField(blank=True, help_text='Jeśli masz zapowiedź wydarzenia w formie wideo, możesz tutaj wstawić. Jeśli prowadzisz live na facebooku, wstaw do niego link, a osoby zainteresowane będą mogły kliknąć "Otrzymaj powiadomienie" bezpośrednio z Żyj świadomie.', null=True, verbose_name='Link do wideo'),
        ),
    ]
