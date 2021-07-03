
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name="Home"),
    path('<int:id>', views.candidateView.as_view(),name="Candidate"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
