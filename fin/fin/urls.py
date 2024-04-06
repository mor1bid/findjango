from django.contrib import admin
from django.urls import path
from recapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', basic, name='basic'),
    path('registration/', regi, name='regi')
]
