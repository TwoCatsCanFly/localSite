from django import forms
from .models import *

choices = Category.objects.all().values_list('name','name')
choice_list = []
for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','description','body','header_image')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value':'',
                                             'id':'elder',
                                             'type':'hidden'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description','body',)

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            }