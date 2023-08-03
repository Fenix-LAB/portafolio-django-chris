from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)

# De este modo se podra interactuar con los modelos dentro del panel de administracion