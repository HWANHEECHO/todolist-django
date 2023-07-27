# -*- coding:utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('createPrac', views.createPrac, name = 'createPrac'),
    path('deletePrac', views.deletePrac, name = 'deletePrac')
]