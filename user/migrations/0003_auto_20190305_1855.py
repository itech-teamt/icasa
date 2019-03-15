# Generated by Django 2.1.7 on 2019-03-05 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20190305_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='re_address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=11, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip',
            field=models.CharField(blank=True, default='', max_length=6, verbose_name='zip code'),
        ),
    ]
