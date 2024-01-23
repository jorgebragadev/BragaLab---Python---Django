
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import logar
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('', logar, name='login'),
    path('usuarios/', include('usuarios.urls')),
    path ('exames/', include('exames.urls')),
    path ('empresarial/', include('empresarial.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
