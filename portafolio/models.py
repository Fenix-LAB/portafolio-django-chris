from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=255)
    image = ImageField(upload_to='portafolio/images/')
    url = URLField(blank=True)

# Las clases creadas aqui seran interpretadas por el ORM como tablas que se usaran en la base de datos
# Cada ves que se crea una nueva tabla (clase), se deben correr las migraciones a la base de datos
