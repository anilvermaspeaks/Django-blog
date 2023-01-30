from . import views
from django.urls import path

urlpatterns = [
    path('', views.starting_page, name="home-page"),
    path('posts', views.posts, name="posts"),
    path('posts/<slug:slug>', views.post_detail, name="post_detail"),
]
