
from django.contrib import admin
from django.urls import path, include
from Kariz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Kariz.urls')),


]
