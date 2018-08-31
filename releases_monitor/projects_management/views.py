from django.shortcuts import render

from .models import ProjectLibrary
from django_tables2 import RequestConfig
from .tables import ProjectLibraryTable
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    table = ProjectLibraryTable(ProjectLibrary.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'projects_management/home.html', {'table': table})
