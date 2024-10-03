# marriage_agency/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from profiles.views import home as profile_views
from . import views
urlpatterns = [
    path('admin', admin.site.urls),  # Маршрут для админ-панели
    path('', views.home, name='home'),  # Маршрут для главной страницы

]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('profiles/', include('profiles.urls')),  # Подключение маршрутов профилей
    path('payments/', include('payments.urls')),
    path('messaging/', include('messaging.urls')),
    path('verification/', include('verification.urls')),
    path('communications/', include('communications.urls')),
)

# Для режима разработки - обслуживать медиафайлы
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)