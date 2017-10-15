"""myproject URL Configuration

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
# from django.conf.urls import *
from django.contrib import admin
# admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/',include('poster.urls')),
    url(r'^$',include('poster.urls')),
    url(r'^approve/',include('approver.urls')),    
    url(r'^online/',include('online.urls')),    
    url(r'^accounts/login/', auth_views.login,name = 'login'),
    url(r'^logout/', auth_views.logout_then_login),
    # url(r'^logout/', auth_views.logout),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# urlpatterns = patterns('',
    # (r'^admin/', admin.site.urls),
    # (r'^login/', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    # (r'^logout/', 'django.contrib.auth.views.logout'),
# )
