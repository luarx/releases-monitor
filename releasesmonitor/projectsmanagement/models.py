from django.db import models
from django.utils import timezone


class Project(models.Model):
    DEV = 'DEV'
    STAGING = 'STAGING'
    RELEASE = 'RELEASE'
    PRO = 'PRO'
    ENVIRONMENT_CHOICES = (
        (DEV, 'Development'),
        (STAGING, 'Staging'),
        (RELEASE, 'Release'),
        (PRO, 'Production'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    repo_url = models.URLField(max_length=200)
    environment = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.environment)


class Library(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    repo_url = models.URLField(max_length=200)
    last_version = models.CharField(max_length=20, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    version_check_date = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "libraries"


class ProjectLibrary(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    current_version = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Library of project"
        verbose_name_plural = "Libraries of projects"
        ordering = ['project']
