import django_tables2 as tables
from .models import ProjectLibrary


class ProjectLibraryTable(tables.Table):
    projectName = tables.Column(accessor='project.name', verbose_name='Project')
    projectEnvironment = tables.Column(accessor='project.environment')
    lastVersion = tables.Column(accessor='library.last_version')
    versionCheckDate = tables.Column(accessor='library.version_check_date')

    class Meta:
        model = ProjectLibrary
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", "creation_date", "project")
        sequence = ('projectName', 'projectEnvironment', 'library',
                    'current_version', 'lastVersion', 'versionCheckDate', '...')
        row_attrs = {
            'class': lambda record: 'version-updated' if record.is_version_updated else 'version-outdated'
        }
