from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from certificate.views import index

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', index, name='home'),
    path('certificate/', include('certificate.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)