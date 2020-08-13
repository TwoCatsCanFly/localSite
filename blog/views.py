from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html',{'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'blog/categories.html',{'category_posts':category_posts,'cats':cats.title().replace('-',' ')})

class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists(): liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked


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

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))