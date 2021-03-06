# Generated by Django 2.1 on 2018-08-31 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('verbose_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('repo_url', models.URLField()),
                ('last_version', models.CharField(blank=True, help_text='Supported formats: X.Y.Z, vX.Y.Z, [sometext]X.Y.Z, X.Y.Z[sometext], [sometext]X.Y.Z[sometext], X.Y, vX.Y, [sometext]X.Y, X.Y[sometext], [sometext]X.Y[sometext]', max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('version_check_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'libraries',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('repo_url', models.URLField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('environment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects_management.Environment')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_version', models.CharField(help_text='Supported formats: X.Y.Z, vX.Y.Z, [sometext]X.Y.Z, X.Y.Z[sometext], [sometext]X.Y.Z[sometext], X.Y, vX.Y, [sometext]X.Y, X.Y[sometext], [sometext]X.Y[sometext]', max_length=20)),
                ('check_mayor_version_update', models.BooleanField(default=True, verbose_name='Check Mayor Update')),
                ('check_minor_version_update', models.BooleanField(default=True, verbose_name='Check Minor Update')),
                ('check_patch_version_update', models.BooleanField(default=False, verbose_name='Check Patch Update')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_management.Library')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects_management.Project')),
            ],
            options={
                'ordering': ['project'],
                'verbose_name_plural': 'Libraries of projects',
                'verbose_name': 'Library of project',
            },
        ),
    ]
