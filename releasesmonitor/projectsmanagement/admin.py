from django.contrib import admin
from .models import Project, Library, ProjectLibrary

admin.site.register(Project)
admin.site.register(Library)
admin.site.register(ProjectLibrary)
