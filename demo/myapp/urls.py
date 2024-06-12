from django.contrib import admin
from django.urls import path,include, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")
]