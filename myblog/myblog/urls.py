from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)