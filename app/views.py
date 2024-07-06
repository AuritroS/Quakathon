from django.shortcuts import render
from .forms import LocationForm
from .models import Location, Campus
import pyrebase

config = {
    "apiKey": "AIzaSyDZ2c-wDusqIz0eEw96NFa9LfE-XyZDvOI",
    "authDomain": "quakathon-35731.firebaseapp.com",
    "databaseURL": "https://quakathon-35731-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "quakathon-35731",
    "storageBucket": "quakathon-35731.appspot.com",
    "messagingSenderId": "196799107729",
    "appId": "1:196799107729:web:de3de57c6d3d9173a9e530",
}

firebase = pyrebase.intialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.


def HomeView(request):
    context = {}

    form = LocationForm(request.POST or None, request.FILES or None)
    locations = None

    if request.method=="POST":
        campus = request.POST['campus']
        locations = Location.objects.filter(campus = campus)

    context['form'] = form
    context['locations']= locations
    return render(request, "index.html", context)