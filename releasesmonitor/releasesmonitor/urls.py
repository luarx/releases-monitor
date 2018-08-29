from django.contrib import admin
from django.urls import include, re_path, path

urlpatterns = [
    re_path(r'^', include('projectsmanagement.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
