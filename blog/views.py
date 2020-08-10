from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-date_created']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')