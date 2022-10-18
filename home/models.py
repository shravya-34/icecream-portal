from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Login(models.Model):
    name = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=30)
    
