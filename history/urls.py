from django.contrib import admin
from django.urls import path, include
from . import views
import history


urlpatterns = [
    path(
        '',
        views.index,
        name='historyIndex')
]
