"""nepalfund URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from __future__ import absolute_import
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^aids/', aids, name='aids'),
    url(r'^infographics/', infographics, name='infographics'),
    url(r'^provideaidinfo/', provideaidinfo, name='provideaidinfo'),
    url(r'^aidsdetails-int/(?P<subcat>\w{0,30})/', aidsdetailsint, name='aidsdetailsint'),
    url(r'^aidsdetails-gov/(?P<subcat>\w{0,30})/', aidsdetailsgov, name='aidsdetailsgov'),
    url(r'^aidsdetails/(?P<donor_id>\d+)/', aidsdetails, name='aidsdetails'),
    url(r'^infographdataint/', infographdataint, name='infographdataint'),
    url(r'^infographdatagov/', infographdatagov, name='infographdatagov'),
    url(r'^infographdatacrowd/', infographdatacrowd, name='infographdatacrowd'),
    url(r'^bydonorname/', bydonorname, name='bydonorname')
    # url(r'^aids/')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)