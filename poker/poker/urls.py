from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^holdem/', include('holdem.urls')),
    url(r'^admin/', include(admin.site.urls)),
]