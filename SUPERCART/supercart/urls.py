from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

# default: "Django Administration"
admin.site.site_header = 'SuperMart'
# default: "Site administration"
admin.site.index_title = 'SuperMart | Admin'
# default: "Django site admin"
admin.site.site_title = 'SuperMart'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
