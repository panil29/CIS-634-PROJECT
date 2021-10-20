"""academicperformance URL Configuration

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
from django.contrib import admin
from django.conf.urls import url

from academic import views as academic_views
urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', academic_views.index, name='index' ),
     url(r'^about/$', academic_views.about, name='about' ),

    url(r'^services/$', academic_views.services, name='services' ),

    url(r'^login/$', academic_views.login, name='login' ),

    url(r'^flogin/$', academic_views.flogin, name='flogin' ),

    url(r'^slogin/$', academic_views.slogin, name='slogin' ),

    url(r'^contact/$', academic_views.contact, name='contact' ),
]
