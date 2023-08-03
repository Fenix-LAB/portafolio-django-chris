from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    # Consulta a la base de datos
    projects = Project.objects.all()
    # print(projects) resultado de la consulta: <QuerySet [<Project: Project object (0)>, <Project: Project object (1)>]>
    return render (request, 'home.html', {'proyects', projects})