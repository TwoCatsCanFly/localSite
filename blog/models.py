from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return  reverse('blog')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500,null=True, blank=True)
    #body = models.TextField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title)+' | '+str(self.author)

    def get_absolute_url(self):
        return  reverse('article-detail', args=(str(self.id)))


    # input_formats='%H:%M:%S %d %B %Y'