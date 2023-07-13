from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.about, name="about"),
    path("blog-posts", views.blogs, name="blog-posts"),
    path("job/<int:job_id>", views.job, name="job"),
    path("category/<str:job_category>", views.job_category, name="category"),
    path("location/<str:job_location>", views.location, name="location"),
    path("search", views.search, name="search"),
    path("blog/<int:blog_id>", views.blog, name="blog"),
    path("blog-search", views.blog_search, name="blog-search"),
    path("type/<str:type_job>", views.type_search, name="type"),
]