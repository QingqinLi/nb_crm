"""nb_crm URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from crm.views import consultant_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crm/', include("crm.urls", namespace="crm")),
    url(r'^logout/', view=consultant_views.logout, name='logout'),
    url(r'^rbac/', include("rbac.urls", namespace="rbac")),
    url(r'^v_code/', view=consultant_views.v_code, name='v_code'),
    url(r'^login/', view=consultant_views.login, name='login'),
]
