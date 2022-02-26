from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("blogs/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("categories/<category>/", views.blog_categories, name="blog_category")
]