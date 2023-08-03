## Aplicacion que se encarga de la funcionalidad del portafolio

#### Models
Primero se definen los modelos con los que se trabajara la base de datos, dentro del archivo de models.py
Los modelos corresponden a tablas que se añaden a la base de datos, el tipo de dato se obtienen del siguiente modulo:

```python
from django.db.models.fields
```

Cada ves que se crea una nueva tabla (clase), se deben correr las migraciones a la base de datos.

Para realizar las migraciones se usa el siguiente comando:
```bash
python manage.py makemigrations
```
Seguido de:
```bash
python manage.py migrate
```

#### Admin
Para poder interactuar con los modelos de base de datos en el panel de administrador se puede realizar el la configuracion en el archivo de admin.py
Para visitar el panel de administracion nos dirijimos a la url: http://127.0.0.1:8000/admin

#### Views
En el archivo de views.py es donde se hace el llamado de los templates html apartir de funciones 