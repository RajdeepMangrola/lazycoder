from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    state= models.CharField(max_length=122)
    zipcode=models.CharField(max_length=122)