from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add-article/', AddPost.as_view(), name='add-article'),
    path('add-category/', AddCategory.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update-article'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete-article'),
    path('category/<str:cats>', CategoryView, name='category'),
    ]
