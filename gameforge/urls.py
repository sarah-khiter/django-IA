from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gameforge.core.urls')),  # Chemin corrigé
    path('users/', include('gameforge.users.urls')),
    path('projects/', include('gameforge.projects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Ajoute cette ligne
]