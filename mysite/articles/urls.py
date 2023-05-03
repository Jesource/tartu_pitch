from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article", views.article, name="article"),
    path("article1", views.article, name="article"),
    path("article2", views.article2, name="article2"),
    path("article3", views.article3, name="article2"),
]
