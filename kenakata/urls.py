from django.contrib import admin
from django.urls import path, include

# import os

# print(os.environ['DJANGO_SETTINGS_MODULE'])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('dashboard/', include('dashboard.urls')),    
]
