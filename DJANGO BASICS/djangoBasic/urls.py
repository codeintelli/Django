"""djangoBasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path

# tesing
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='home'),
#     path('html/', views.usingHtml, name='html'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('analyze', views.analyze, name='analyze'),
    path('capitalizefirst/', views.capitalizefirst, name='capitalizefirst'),
    path('newlineremove/', views.newlinemove, name='newlinemove'),
    path('spaceremover/', views.spaceremover, name='spaceremover'),
    path('charcount/', views.charcount, name='charcount'),
]


