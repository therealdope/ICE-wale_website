from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("bar", views.bar, name="home"),
    path("sundae", views.sundae, name="sundae"),
    path("cone", views.cone, name="cone"),
    path("cake", views.cake, name="cake"),
    path("list", views.list, name="list"),
    path('toggle-list/<int:image_id>/', views.toggle_list, name='toggle_list'),
]