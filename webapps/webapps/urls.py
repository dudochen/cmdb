"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

import xadmin
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

#from assets.urls import router as assets_router
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title="CMDB API")


urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',  xadmin.site.urls),
    #url(r'^user/', include('users.urls', namespace='user')),
    #url(r'^navi/', include('navi.urls', namespace='navi')),
    #url(r'^permission/', include('permission.urls', namespace='permission')),
    #url(r'^asset/', include('assets.urls', namespace='assets')),
    #url(r'^domain/', include('domain.urls', namespace='domain')),
]
