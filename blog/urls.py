from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add-article/', AddPost.as_view(), name='add-article'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update-article'),
    ]
