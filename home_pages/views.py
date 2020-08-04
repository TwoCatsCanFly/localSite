from django.shortcuts import render

# Create your views here.
def localWeather(request):

    return render(request, 'localWeather/home.html')