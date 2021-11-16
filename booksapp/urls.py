from django.urls import path
from booksapp.views import *

urlpatterns=[
    path('',show),
    path('showinfo',showinfo),
]