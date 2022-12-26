from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Home.views import homepage
from Products.views import carslist , carsingle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('cars/', carslist),
    path('cars/carsingle/<int:car_id>', carsingle)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)