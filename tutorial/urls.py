"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views as quickstartviews
from snippets import views as snippetsviews
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')
router = routers.DefaultRouter()
router.register(r'users', snippetsviews.UserViewSet)
router.register(r'groups', quickstartviews.GroupViewSet)
router.register(r'snippet', snippetsviews.SnippetViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
     url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]

