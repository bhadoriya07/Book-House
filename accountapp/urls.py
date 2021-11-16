from django.urls import path
from accountapp.views import *

urlpatterns=[
    path('login',login),
    path('signup',signup),
    path('home',home),
    path('show_main',show_main),
]