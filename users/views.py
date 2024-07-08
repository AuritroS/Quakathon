from django.shortcuts import render, redirect
from django.contrib import messages
from app import views

def profile(request):
    return render(request, 'profile.html')