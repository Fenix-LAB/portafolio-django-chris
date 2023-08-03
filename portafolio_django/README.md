## Dentro de este folder se encuantra la configuracion del proyecto, en este caso es el proyecto del portafolio.

#### Admin
Para tener acceso a la pestaña de adminic=stracion se necesita un usuario, se crea con el comando de:
```bash
python manage.py createsuperuser
```

#### Settigs
Dentro del archivo de settings.py en la seccion de INSTALLED_APPS se colocan las aplicaciones que se vyan creando con el comando de :
```bash
python manage.py startapp {name app}
```

Ejemplo:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'portafolio',
]
```

En este proyecto se usara una carpeta de imagenes asi que se debe declarar com un static file dentro de settongs.py

```python
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

#### Urls
Y el llamado de los archivos estaticos se hace en el archivo de urls.py con:

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'
```

Dentro de urls tambien se configuran todas las rutas del proyecto