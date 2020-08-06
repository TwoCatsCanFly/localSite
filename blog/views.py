from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *
from .forms import *

# Create your views here.
class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'

class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'
    #fields = ('title','body')

class UpdatePost(UpdateView):
    model = Post
    fields = ('title','body','description')
    template_name = 'blog/update_post.html'