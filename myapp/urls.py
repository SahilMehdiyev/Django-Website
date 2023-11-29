from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact, name='contact'),
    path('downloadFile/',views.downloadFile,name='downloadFile'),
    path('downloadFilePptx/',views.downloadFilePptx,name='downloadFilePptx')
    # path('content',views.content,name='content')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

