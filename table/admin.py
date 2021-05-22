from django.contrib import admin
from .models import Queue, Name, Group

admin.site.register(Queue)
admin.site.register(Name)
admin.site.register(Group)