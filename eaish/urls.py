from django.contrib import admin
from django.urls import path
from django.urls.conf import include



urlpatterns = [
    path('raushan/', admin.site.urls),
    path('',include('home.urls'))
]
