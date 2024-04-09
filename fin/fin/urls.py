from django.contrib import admin
from django.urls import path
from recapp.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', basic, name='basic'),
    path('regi.html/', regi, name='regi'),
    # path('login.html/', login, name='login'),
    path('login.html/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('mkdish.html/', mkdish, name='mkdish')
]
