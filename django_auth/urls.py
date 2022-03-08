from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.urls import *
from django_auth.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')), # now we get lots of urls available
    path('admin/', admin.site.urls),
]