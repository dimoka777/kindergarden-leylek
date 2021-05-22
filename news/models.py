from django.db import models
from django.urls import reverse
from _datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Жаңылыктын Аты')
    body = models.TextField(verbose_name='Жаңылык')
    photo = models.ImageField(upload_to='images/', default='images/def.jpg', blank=True,
                              verbose_name='Сүрөт')
    post_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])
