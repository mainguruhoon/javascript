
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App',include('App.urls')),
    path('App2',include('App2.urls')),
]
