"""
project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import  StaticViewSitemap, NewsSitemap
from django.contrib.sitemaps import views

sitemaps = {
    'static': StaticViewSitemap,
    'News': NewsSitemap
}
admin.site.site_header = '3la Bal'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps} ,name='sitemap'),
    path('sitemap-<section>.xml', views.sitemap, {
        'sitemaps': sitemaps,
        'template_name': 'custom_sitemap.html'
    }, name='django.contrib.sitemaps.views.sitemap'),

]
