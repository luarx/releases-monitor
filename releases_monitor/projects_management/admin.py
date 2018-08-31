from django.contrib import admin
from .models import Project, Library, ProjectLibrary, Environment

admin.site.register(Project)
admin.site.register(Library)
admin.site.register(ProjectLibrary)
admin.site.register(Environment)
