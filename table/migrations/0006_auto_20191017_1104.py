# Generated by Django 2.2.5 on 2019-10-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_group_group_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='about_text',
            field=models.CharField(max_length=255, verbose_name='Тайпана жөнүндө маалымат'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=20, verbose_name='Тайпанын аты'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_reg',
            field=models.IntegerField(verbose_name='Окуучулардын саны'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_teachers',
            field=models.CharField(max_length=20, verbose_name='Мугалимдердин саны'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_year_from',
            field=models.PositiveIntegerField(verbose_name='Жылдан баштап'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_year_to',
            field=models.PositiveIntegerField(verbose_name='Жылга чейин'),
        ),
    ]
