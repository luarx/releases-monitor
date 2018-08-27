import django_tables2 as tables
from .models import ProjectLibrary

class ProjectLibraryTable(tables.Table):
    lastVersion = tables.Column(accessor='library.last_version')
    versionCheckDate = tables.Column(accessor='library.version_check_date')

    class Meta:
        model = ProjectLibrary
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", "creation_date",)
