# Generated by Django 2.1.5 on 2019-09-12 16:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
                ('group_year_from', models.PositiveIntegerField()),
                ('group_year_to', models.PositiveIntegerField()),
                ('about_text', models.CharField(max_length=255)),
                ('group_reg', models.IntegerField()),
                ('group_teachers', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garden_name', models.CharField(max_length=30)),
                ('garden_address', models.CharField(max_length=50)),
                ('garden_phone', models.CharField(max_length=20)),
                ('garden_email', models.CharField(max_length=20)),
                ('garden_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=200, verbose_name='Баланын Аты-Жөнү')),
                ('child_gender', models.CharField(choices=[('Erkek', 'Уул'), ('Kyz', 'Кыз')], max_length=10, verbose_name='Баланын жыныс')),
                ('child_birthday', models.DateField(verbose_name='Баланын Туулган күнү')),
                ('birth_certificate', models.CharField(max_length=15, verbose_name='Туулгандыгы туралуу Күболүктүн номери')),
                ('custom_given_certificate', models.CharField(max_length=15, verbose_name='Күбөлүктүү берген Орган')),
                ('certificate_given_date', models.DateField(verbose_name='Күбөлүктү берген күнү')),
                ('child_address', models.CharField(max_length=255, verbose_name='Дарек')),
                ('parent_name', models.CharField(max_length=255, verbose_name='Ата-Энесинин Аты-Жөнү')),
                ('parent_phone', models.CharField(max_length=20, verbose_name='Телефону')),
                ('registration_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Арызы катталган күнү')),
                ('choice_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='groups', to='table.Group')),
            ],
        ),
    ]
