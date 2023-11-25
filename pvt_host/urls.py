from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Add this import for the static function

urlpatterns = [
    path("admin", admin.site.urls),
    path('', include('home.urls')),
    path('hostel', include('home.urls')),
]


