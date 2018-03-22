"""blog_s19 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.views.static import serve
from blog_s19 import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login),
    url(r'^get_valid_img/',views.get_valid_img),
    url(r'^index/',views.index),
    url(r'^register/',views.register),
    url(r'^$',views.index),
    url(r'^logout/$',views.log_out),

    #blog分发
    url(r'^blog/',include('blog.urls')),
    #media配置
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #文本编辑器上传
    url(r'^upload_img/',views.upload_img),


]
