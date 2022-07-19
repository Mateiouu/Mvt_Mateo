
from django.contrib import admin
from django.urls import path, include
from Familiares.views import *



urlpatterns = [
     path('admin/', admin.site.urls),
    path('app-familiares/', include('Familiares.urls')),
    
]
