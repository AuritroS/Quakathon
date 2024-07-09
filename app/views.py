from django.shortcuts import render
from .forms import LocationForm
from .models import Location



def HomeView(request):
    return render(request, "index.html", )

def MapView(request):
    return render(request, "map.html")

def ProfileView(request):
    return render(request, "profile.html")

def CreateGroupView(request):
    return render(request, "creategroup.html")

def JoinGroupView(request):
    return render(request, "joingroup.html")

def FriendsView(request):
    return render(request, "friends.html")

def PointsView(request):
    return render(request, "points.html")