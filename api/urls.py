
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^user/', views.index),
    url(r'^link/', views.link_index),
]
