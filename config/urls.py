from django.contrib import admin
from django.urls import include, re_path, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^', include('releases_monitor.projects_management.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
