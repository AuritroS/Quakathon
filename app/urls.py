from django.urls import path 
from . import views 


urlpatterns = [
    # path('', views.HomeView, name='home'),
    path('', views.MapView, name='map'),
    path('friends/', views.FriendsView, name='friends'),
    path('profile/', views.ProfileView, name='profile'),
    path('create-group/', views.CreateGroupView, name='create-group'),
    path('join-group/', views.JoinGroupView, name='join-group'),
    path('points/', views.PointsView, name='points'),

]