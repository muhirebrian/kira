import imp 
from xml.dom.minidom import Document
from django.urls import path
from .import views                      
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='login'),
    path('registration/',views.registration, name='registration'),
    path('forgotpassword/',views.forgotpassword, name='forgotpassword'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/',views.contactus, name='contactus'),
    path('index/',views.index, name='index')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
