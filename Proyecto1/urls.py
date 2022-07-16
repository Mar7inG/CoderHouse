from django.contrib import admin
from django.urls import path
from Proyecto1.views import template1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Templa/', template1 ),
]
