from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
from .models import *


def index(request):

    # Jobs
    jobs = Job.objects.all()
    jobs = jobs.order_by("-timestamp").all() 
    featured_jobs = jobs[:6]

    # Blogovi
    blogs = Blog.objects.all()
    blogs = blogs.order_by("-timestamp").all() 
    blogs = blogs[:3]

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(jobs, 5)
    try:
        p_jobs = paginator.page(page)
    except PageNotAnInteger:
        p_jobs = paginator.page(1)
    except EmptyPage:
        p_jobs = paginator.page(paginator.num_pages)

    return render(request, "stud_poslovi/index.html", {
        "jobs": p_jobs,
        "featured": featured_jobs,
        "blogs": blogs,
    })

def about(request):
    return render(request, "stud_poslovi/about.html")

def blogs(request):

    # Blogs
    blogs = Blog.objects.all()
    blogs = blogs.order_by("-timestamp").all() 

    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(blogs, 5)
    try:
        p_blogs = paginator.page(page)
    except PageNotAnInteger:
        p_blogs = paginator.page(1)
    except EmptyPage:
        p_blogs = paginator.page(paginator.num_pages)
    return render(request, "stud_poslovi/blog-posts.html", {
        "blogs": p_blogs,
    })

def job(request, job_id):
    job = Job.objects.get(pk=job_id)
    print(job)
    return render(request, "stud_poslovi/single_job.html", {
        "job": job,
    })

def job_category(request, job_category):
    category_job = Job.objects.filter(category=job_category)
    if category_job:
        empty_page = False
    else:
        empty_page=True

    blogs = Blog.objects.all()
    blogs = blogs.order_by("-timestamp").all() 
    blogs = blogs[:3]
    return render(request, "stud_poslovi/category.html", {
        "jobs": category_job,
        "category": job_category,
        "empty": empty_page,
        "blogs": blogs,
    })

def location(request, job_location):
    location_job = Job.objects.filter(location__icontains=job_location)
    print(location_job)
    if location_job:
        empty_page = False
    else:
        empty_page=True

    return render(request, "stud_poslovi/category.html", {
        "jobs": location_job,
        "empty_location": empty_page,
        "location": job_location,
    })

def search(request):
    if request.method == "POST":
        if request.POST["search"]:
            search_jobs = Job.objects.filter(title__icontains=str(request.POST["search"]))
        else:
            search_jobs = Job.objects.all()
        blogs = Blog.objects.all()
        blogs = blogs.order_by("-timestamp").all() 
        blogs = blogs[:3]
        return render(request, "stud_poslovi/category.html", {
        "jobs": search_jobs,
        "blogs":blogs,
        "search":True,
    })

def blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)

    blogs = Blog.objects.all()
    blogs = blogs.order_by("-timestamp").all() 
    blogs = blogs[:4]
    return render(request,"stud_poslovi/blog_single.html", {
        "blog": blog,
        "blogs": blogs,
    })
    
def blog_search(request):
    if request.method == "POST":
        if request.POST["search2"]:
            search_blogs = Blog.objects.filter(title__icontains=str(request.POST["search2"]))
            search_blogs = search_blogs.order_by("-timestamp").all() 
        else:
            search_blogs = Blog.objects.all()
            search_blogs = search_blogs.order_by("-timestamp").all()
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(search_blogs, 5)
        try:
            p_blogs = paginator.page(page)
        except PageNotAnInteger:
            p_blogs = paginator.page(1)
        except EmptyPage:
            p_blogs = paginator.page(paginator.num_pages)
        return render(request, "stud_poslovi/blog-posts.html", {
            "blogs": p_blogs,
        })

def type_search(request, type_job):
    type_jobs = Job.objects.filter(type=type_job)
    if type_jobs:
        empty_page = False
    else:
        empty_page=True

    blogs = Blog.objects.all()
    blogs = blogs.order_by("-timestamp").all() 
    blogs = blogs[:3]
    return render(request, "stud_poslovi/category.html", {
        "jobs": type_jobs,
        "empty": empty_page,
        "blogs": blogs,
        "type":type_job,
    })