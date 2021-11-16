from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from donatorapp.models import Donator_Books, donator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from donatorapp.models import donator
from django.contrib.auth.hashers import check_password,make_password
import json

def dlogout(request):
    if request.session.has_key('email'):
        del request.session['email']
        return render(request, 'booksapp/index.html')
    else:
        data = {}
        data['message'] = "Please submit the Login Form"
        return render(request, 'booksapp/index.html', data)


def delete(request):
    if request.session.has_key('email'):
        email_id = request.session['email']
        classes = request.POST['classes']
        subject = request.POST['subjects']
        data = Donator_Books.objects.filter(emai=email_id, subjects=subject, for_class=classes)
        data.delete()
        return redirect('/donatorapp/showbook')
    else:
        data = {}
        data['message'] = "Please submit the Login Form"
        return render(request, 'booksapp/index.html', data)

    


def showbook(request):
    if request.session.has_key('email'):
        email_id = request.session['email']
        da = Donator_Books.objects.filter(emai=email_id)
        content = {
            'data': da,
        }
        return render(request, 'booksapp/donator.html', content)
    else:
        return render(request, 'booksapp/index.html')


def savebook(request):
    if request.session.has_key('email'):

        subjects = request.POST['subjects']
        for_class = request.POST['book_class']
        number_of_books = request.POST['book_no']
        edition = request.POST['edition']
        image = request.FILES['img']
        emai = request.session['email']
        dno=Donator_Books(subjects=subjects,for_class=for_class,edition=edition,image=image,number_of_books=number_of_books,emai=emai)
        dno.save()
        return redirect('/donatorapp/showbook')
    else:
        return render(request, 'booksapp/index.html')


def dlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        pword = request.POST['password']
        dno=donator.objects.get(emai=email)
        valid=check_password(pword,dno.passw)
        if valid is not True:
            data = {}
            data['message'] = "Email or Password is incorrect"
            return render(request, 'booksapp/index.html', data)
        else:
            request.session['email'] = email
            return redirect("/donatorapp/showbook")
    else:
        data = {}
        data['message'] = "Please submit the Login Form"
        return render(request, 'booksapp/index.html', data)
 


def dsignup(request):
    if request.method == "POST":
        dno = donator()
        dno.emai = request.POST["email"]
        passw = request.POST['password']
        dno.fname = request.POST['fname']
        dno.lname = request.POST['lname']
        dno.city=request.POST['city']
        dno.number=request.POST['number']
        dno.passw=make_password(passw)
        dno.save()
        data = {}
        data['message'] = "Login to continue"
        return render(request, 'booksapp/index.html', data)
    else:
        data = {}
        data['message'] = "Please submit the SignUp Form"
        return render(request, 'booksapp/index.html', data)