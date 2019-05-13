from django.contrib import admin
from .models import Project, Library, ProjectLibrary, Environment

class ProjectLibraryAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin/project_library/checkbox-version-numbers.js', )

admin.site.register(Project)
admin.site.register(Library)
admin.site.register(ProjectLibrary, ProjectLibraryAdmin)
admin.site.register(Environment)
