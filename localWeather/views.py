from django.shortcuts import render
import os, requests, json

# Create your views here.
def localWeather(request):
    global context
    try:
        api_key = str(os.getenv('OPENWEATHERMAP_API_KEY'))
        city = 'London'
        country = 'uk'
        unit = 'metric'
        api_r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={unit}&appid={api_key}')
        global api
        api = json.loads(api_r.content)
        for d in api: print(f'{d}: {api[d]}')
    except Exception as err:
        api = {'cod':'404'}
        print(f'Ошибка!: {err}')

    if api['cod'] != '404':
        context = {'coord_lon':api['coord']['lon'],
                   'coord_lat': api['coord']['lat'],
                   'temp': api['main']['temp'],
                   'temp_feels': api['main']['feels_like'],
                   'temp_min': api['main']['temp_min'],
                   'temp_max': api['main']['temp_max'],
                   'pressure': api['main']['pressure'],
                   'humidity': api['main']['humidity'],
                   'visibility': api['visibility'],
                   'wind_speed': api['wind']['speed'],
                   'wind_dir': api['wind']['deg'],
                   'clouds': api['clouds']['all'],
                   'time_updated': api['dt'],
                   'country': api['sys']['country'],
                   'sunrise_time': api['sys']['sunrise'],
                   'sunset_time': api['sys']['sunset'],
                   'timezone': api['timezone'],
                   'city_id': api['id'],
                   'city_name': api['name'],
                   'cod': api['cod'],

                   }
    else: context = {'cod':api['cod']}
    print(f'API responce: {api}')
    if api.setdefault('rain',None):
        apt = list(api['rain'].keys())
        if '1h' in apt:
            context.update({'rain_1h': api['rain']['1h']})
        elif '3h' in apt:
            context.update({'rain_3h': api['rain']['3h']})
    if api.setdefault('snow',None):
        apts = list(api['snow'].keys())
        if '1h' in apts:
            context.update({'snow_1h': api['snow']['1h']})
        elif '3h' in apts:
            context.update({'snow_3h': api['snow']['3h']})
    print(f'Context values: {context}')
    return render(request, 'localWeather/index.html',context)
