from django.shortcuts import render

from projectsmanagement.models import ProjectLibrary
from django_tables2 import RequestConfig
from .tables import ProjectLibraryTable

def project_library(request):
    table = ProjectLibraryTable(ProjectLibrary.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'projectsmanagement/projectlibrary_list.html', {'table': table})
