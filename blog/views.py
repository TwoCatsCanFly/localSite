from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.
class Blog(ListView):
    model = Post
    template_name = 'blog.html'
