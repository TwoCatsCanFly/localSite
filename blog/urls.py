from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    ]
