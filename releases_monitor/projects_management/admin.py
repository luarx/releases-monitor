from django.contrib import admin
from .models import Project, Library, ProjectLibrary, Environment

class ProjectLibraryAdmin(admin.ModelAdmin):
    list_display = ['project', 'library', 'current_version']

    class Media:
        js = ('js/admin/project_library/checkbox-version-numbers.js', )

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_version', 'last_version_date']

admin.site.register(Project)
admin.site.register(ProjectLibrary, ProjectLibraryAdmin)
admin.site.register(Environment)
