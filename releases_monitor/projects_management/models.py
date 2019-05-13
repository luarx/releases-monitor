from django.db import models
from django.utils import timezone

import re


class Environment(models.Model):
    name = models.CharField(max_length=15)
    verbose_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    repo_url = models.URLField(max_length=200, blank=True)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}//{}".format(self.name, self.environment)


class Library(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    repo_url = models.URLField(max_length=200)
    last_version = models.CharField(
        max_length=20, blank=True, help_text="Supported formats: X.Y.Z, vX.Y.Z, [sometext]X.Y.Z, X.Y.Z[sometext], [sometext]X.Y.Z[sometext], X.Y, vX.Y, [sometext]X.Y, X.Y[sometext], [sometext]X.Y[sometext]")
    creation_date = models.DateTimeField(auto_now_add=True)
    version_check_date = models.DateTimeField(null=True, auto_now=True)
    last_version_date = models.DateTimeField(null=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "libraries"


class ProjectLibrary(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    current_version = models.CharField(
        max_length=20, help_text="Supported formats: X.Y.Z, vX.Y.Z, [sometext]X.Y.Z, X.Y.Z[sometext], [sometext]X.Y.Z[sometext], X.Y, vX.Y, [sometext]X.Y, X.Y[sometext], [sometext]X.Y[sometext]")
    check_mayor_version_update = models.BooleanField(
        default=True, verbose_name="Check Mayor Update")
    check_minor_version_update = models.BooleanField(
        default=True, verbose_name="Check Minor Update")
    check_patch_version_update = models.BooleanField(
        default=False, verbose_name="Check Patch Update")
    creation_date = models.DateTimeField(auto_now_add=True)

    @property
    def is_version_updated(self):
        def is_mayor_version_updated(current, last_version):
            return current == last_version

        def is_minor_version_updated(current, last_version):
            return current == last_version

        def is_patch_version_updated(current, last_version):
            return current == last_version

        if self.library.last_version:
            regex_current_version = re.search(
                '\D*(?P<mayor>\d*)\.(?P<minor>\d*)(\.(?P<patch>\d*))?.*$', self.current_version)

            regex_last_version = re.search(
                '\D*(?P<mayor>\d*)\.(?P<minor>\d*)(\.(?P<patch>\d*))?.*$', self.library.last_version)

            if self.check_patch_version_update:
                return is_mayor_version_updated(regex_current_version.group('mayor'), regex_last_version.group('mayor'))\
                and is_minor_version_updated(regex_current_version.group('minor'), regex_last_version.group('minor'))\
                and is_patch_version_updated(regex_current_version.group('patch'), regex_last_version.group('patch'))
            elif self.check_minor_version_update:
                return is_mayor_version_updated(regex_current_version.group('mayor'), regex_last_version.group('mayor'))\
                and is_minor_version_updated(regex_current_version.group('minor'), regex_last_version.group('minor'))
            elif self.check_mayor_version_update:
                return is_mayor_version_updated(regex_current_version.group('mayor'), regex_last_version.group('mayor'))
            else:
                return True

        else:
            return None

    def __str__(self):
        return "{} -- {}".format(self.project, self.library)

    class Meta:
        verbose_name = "Library of project"
        verbose_name_plural = "Libraries of projects"
        ordering = ["project"]
