# Generated by Django 2.1.7 on 2019-03-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190302_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='click',
            field=models.IntegerField(default=0, verbose_name='the number of clicks of a product'),
        ),
    ]
