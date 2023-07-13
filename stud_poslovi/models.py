from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField 

class User(AbstractUser):
    pass

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(default="description")
    requirements = RichTextField(default="requirements")
    contact = models.CharField(max_length=2000)
    description_of_the_potential_candidate = RichTextField(default="potential")
    image = models.CharField(max_length=3000)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Bosna i Hercegovina")
    short = RichTextField(default="short")

class Blog(models.Model):
    author = models.CharField(max_length=200, default="author")
    author_education = models.CharField(max_length=1000, default="zanimanje")
    tag = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    intro = RichTextField(default="short intro")
    description = RichTextField(default="blog content")
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=5000, default="pic")



