from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('blogpost/<str:slug>/', views.blogpost, name='blogpost'),
    path('category/<str:category>', views.category, name='category'),
    path('create/', views.create_blog, name='create_blog'),
    
]