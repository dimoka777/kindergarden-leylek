# Generated by Django 2.2.5 on 2019-10-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_auto_20191017_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='garden_end',
            field=models.CharField(default=1, max_length=20, verbose_name='Бала бакчанын жабылуу убакыты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='name',
            name='garden_map_lat',
            field=models.CharField(default=1, max_length=30, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='name',
            name='garden_map_lon',
            field=models.CharField(default=1, max_length=30, verbose_name='Долгота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='name',
            name='garden_start',
            field=models.CharField(default=1, max_length=20, verbose_name='Бала бакчанын ачылуу убакыты'),
            preserve_default=False,
        ),
    ]