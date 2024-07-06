from django.shortcuts import render
from .forms import LocationForm
from .models import Location, Campus

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