from django.shortcuts import render

# Create your views here.

import urllib
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city_fix = city.replace(' ','%20')
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city_fix + '&units=metric&appid=ee53ee7a0c3c6e15dfbc8f00d69f6c9e').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)