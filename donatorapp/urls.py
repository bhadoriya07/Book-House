from django.urls import path
from donatorapp.views import *

urlpatterns=[
    path('signup',dsignup),
    path('login',dlogin),
    path('savebook',savebook),
    path('showbook',showbook),
    path('delete',delete),
    path('logout',dlogout),
]