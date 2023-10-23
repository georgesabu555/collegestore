from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from collegeproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("collegeapp.urls")),
    path('credentials/',include('credentials.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)