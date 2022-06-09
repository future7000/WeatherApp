from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def home(request):
    
    if request.method == 'POST':

        city = request.POST['city']
        # retrieve imformation from weather api = https://api.openweathermap.org/api
        try:
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+
            city+'&units=metric&appid=bb41f17afff7f2cd357fef03a739ea8c').read()
            
            # convert  json file into python dectionary
            list_of_data =json.loads(source)

            data ={
                'country_code':str(list_of_data['sys']['country']),
                'cor':str(list_of_data["coord"]["lon"])+" "+str(list_of_data["coord"]["lat"]),
                'temp':str(list_of_data["main"]['temp']),
                'pressure':str(list_of_data['main']["pressure"]),
                'humidity':str(list_of_data['main']['humidity']),
                'main':str(list_of_data["weather"][0]['main']),
                'description':str(list_of_data["weather"][0]['description']),
                'icon':list_of_data["weather"][0]['icon'],
                'city':city
            }
        except:
            return render(request, 'error.html')
    else:
        data ={}
    return render(request,'weather.html',data)


def index(request):
    return render(request,'index.html')
