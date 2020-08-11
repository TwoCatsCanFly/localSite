from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class Blog(ListView):
    model = Post
    template_name = 'blog/blog.html'
    cats = Category.objects.all()
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Blog, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))

    return render(request, 'blog/categories.html',{'category_posts':category_posts,'cats':cats.title().replace('-',' ')})

class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

class AddCategory(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')