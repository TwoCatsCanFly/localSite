from django.shortcuts import render

# Create your views here.
def home_pages(request):

    return render(request, 'home_pages/home.html')