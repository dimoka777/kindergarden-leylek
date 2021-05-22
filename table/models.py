from django.db import models
from django.urls import reverse
from _datetime import datetime


class Group(models.Model):
    group_name = models.CharField(max_length=20, verbose_name='Тайпанын аты')
    group_year_from = models.PositiveIntegerField(verbose_name='Жылдан баштап')
    group_year_to = models.PositiveIntegerField(verbose_name='Жылга чейин')
    about_text = models.CharField(max_length=255, verbose_name='Тайпана жөнүндө маалымат')
    group_reg = models.IntegerField(verbose_name='Окуучулардын саны')
    group_teachers = models.CharField(max_length=20, verbose_name='Мугалимдердин саны')
    group_img = models.ImageField(upload_to='images/', default='images/def.jpg', blank=True,
                                  verbose_name='Тайпанын cүрөтү')

    def __str__(self):
        return f'{self.group_name}'


class Queue(models.Model):
    CHILD_GENDER = [
        ('Erkek', 'Уул'),
        ('Kyz', 'Кыз')
    ]

    child_name = models.CharField(max_length=200,
                                  verbose_name='Баланын Аты-Жөнү')
    child_gender = models.CharField(max_length=10, choices=CHILD_GENDER,
                                    verbose_name='Баланын жыныс')
    child_birthday = models.DateField(verbose_name='Баланын Туулган күнү')
    birth_certificate = models.CharField(max_length=15,
                                         verbose_name='Туулгандыгы туралуу Күболүктүн номери')
    custom_given_certificate = models.CharField(max_length=15,
                                                verbose_name='Күбөлүктүү берген Орган')
    certificate_given_date = models.DateField(verbose_name='Күбөлүктү берген күнү')
    child_address = models.CharField(max_length=255, verbose_name='Дарек')
    parent_name = models.CharField(max_length=255, verbose_name='Ата-Энесинин Аты-Жөнү')
    parent_phone = models.CharField(max_length=20, verbose_name='Телефону')
    registration_date = models.DateTimeField(default=datetime.now,
                                             verbose_name='Арызы катталган күнү')
    choice_group = models.ForeignKey(Group, related_name='groups', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return '{}{}{}'.format(self.child_name, self.child_birthday,
                               self.custom_given_certificate, )

    def get_absolute_url(self):
        return reverse('queue', args=[str(self.id)])


class Name(models.Model):
    garden_name = models.CharField(max_length=30, verbose_name="Бала бакчанын аты")
    garden_address = models.CharField(max_length=50, verbose_name="Бала бакчанын дареги")
    garden_phone = models.CharField(max_length=20, verbose_name="Бала бакчанын телефону")
    garden_email = models.CharField(max_length=20, verbose_name="Бала бакчанын почтасы")
    garden_info = models.TextField(verbose_name="Бала бакча жөнүндө маалымат")
    garden_start = models.CharField(max_length=20, verbose_name="Бала бакчанын ачылуу убакыты")
    garden_end = models.CharField(max_length=20, verbose_name="Бала бакчанын жабылуу убакыты")
    garden_map_lat = models.CharField(max_length=30, verbose_name="Широта")
    garden_map_lon = models.CharField(max_length=30, verbose_name="Долгота")

    def get_absolute_url(self):
        return reverse('name', args=[str(self.id)])

    def __str__(self):
        return '{}'.format(self.garden_name)
