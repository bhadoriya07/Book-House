from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from donatorapp.models import Donator_Books


def show_main(request):
    if request.session.has_key('email'):
        books = Donator_Books.objects.all()
        data = {'book': books}
        return render(request, 'booksapp/main.html', data)
    else:
        data = {}
        data['message'] = "Please submit the Login Form"
        return render(request, 'booksapp/index.html', data)


def home(request):
    if request.session.has_key('email'):
        books = Donator_Books.objects.all()
        data = {'book': books}
        return render(request, 'booksapp/main.html', data)
    else:
        data = {}
        data['message'] = "Please submit the Login Form"
        return render(request, 'booksapp/index.html', data)


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pword = request.POST['password']
        user = authenticate(request, username=email, password=pword)
        if user is not None:
            auth.login(request, user)
            request.session['email'] = email
            return redirect("/accountapp/show_main")
        else:
            data = {}
            data['message'] = "Email or Password is incorrect"
            return render(request, 'booksapp/index.html', data)
    else:
        data = {}
        data['message'] = "Please submit the Login Form"
        return render(request, 'booksapp/index.html', data)


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        pword = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        data = {}
        if User.objects.filter(username=email).exists():
            data['message'] = "User already exist"
        else:
            user = User.objects.create_user(
                username=email, password=pword, first_name=fname, last_name=lname)
            data['message'] = "Login to continue"
        return render(request, 'booksapp/index.html', data)
    else:
        data = {}
        data['message'] = "Please submit the SignUp Form"
        return render(request, 'booksapp/index.html', data)
