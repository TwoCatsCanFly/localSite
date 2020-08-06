from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500,null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.title)+' | '+str(self.author)

    def get_absolute_url(self):
        return  reverse('article-detail', args=(str(self.id)))


    # input_formats='%H:%M:%S %d %B %Y'