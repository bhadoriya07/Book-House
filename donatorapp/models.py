from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class donator(models.Model):
    fname=models.TextField(max_length=20,)
    lname=models.TextField(max_length=20,)
    emai=models.EmailField()
    passw=models.TextField(max_length=300,)
    city=models.CharField(max_length=20,default="Not provided")
    number=models.IntegerField(default="00000")
    

    def __str__(self):
        return self.fname

class Donator_Books(models.Model):
    emai=models.EmailField(null=True,default=1)
    for_class=models.CharField(max_length=10)
    subjects=models.TextField(max_length=50,default="Not provided",null=True)
    number_of_books=models.CharField(max_length=10)
    edition=models.CharField(max_length=10)
    image=models.ImageField(upload_to="media")

    def __str__(self):
        return self.emai
