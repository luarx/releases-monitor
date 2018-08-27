from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_library, name='project-library-list'),
]
