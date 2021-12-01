from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('tawjih/', views.tawjih ,name='tawjih'),
    path('anapec/', views.anapec ,name='anapec'),
    path('stage/', views.stage ,name='stage'),
    path('talaba/', views.talaba ,name='talaba'),
    path('jobs/', views.jobs ,name='jobs'),
    path('maroc/<str:city>/', views.city ,name='city'),
    path('article/<str:slug>/', views.article ,name='article'),
    path('teq/', views.teq ,name='teq'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'website.views.handler404'
