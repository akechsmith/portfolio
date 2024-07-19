from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from home.models import Blog
from .forms import BlogForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
import random
import re

# Create your views here.
def index (request):
    blogs = Blog.objects.all()
    random_blogs = random.sample(list(blogs), 3)
    context = {'random_blogs': random_blogs}
    return render(request, 'index.html', context)

def about (request):
    return render(request, 'about.html')

def contact(request): 
    return render(request, 'contact.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def projects(request):
    return render(request, 'projects.html')

    
def blogpost (request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {'blog': blog}
        return render(request, 'blogpost.html', context)
    except Blog.DoesNotExist:
        context = {'message': 'Blog post not found'}
        return render(request, '404.html', context, status=404)


def category(request, category):
    category_posts = Blog.objects.filter(category=category).order_by('-time')
    if not category_posts:
        message = f"No posts found in category: '{category}'"
        return render(request, "category.html", {"message": message})
    paginator = Paginator(category_posts, 3)
    page = request.GET.get('page')
    category_posts = paginator.get_page(page)
    return render(request, "category.html", {"category": category, 'category_posts': category_posts})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog post created successfully')
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})
