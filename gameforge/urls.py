from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gameforge.core.urls', namespace='core')),
    path('users/', include('gameforge.users.urls')),
    path('projects/', include('gameforge.projects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Ajoute cette ligne
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)