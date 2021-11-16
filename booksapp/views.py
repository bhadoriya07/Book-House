from django.shortcuts import render
from donatorapp.models import donator



def show(request): return render(request, 'booksapp/index.html')

def showinfo(request):
    email = request.POST['email']
    detail = donator.objects.filter(emai=email)
    data = {'details': detail[0]}
    return render(request, 'booksapp/info.html', data)
