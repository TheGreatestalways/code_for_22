from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_advertisments.urls')),
    path('', include('app_lesson_4.urls')),
]
