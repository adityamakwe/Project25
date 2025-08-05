from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index),
    path('<page>/',views.action),
    path('<page>/<operation>/<int:id>',views.action),
]
