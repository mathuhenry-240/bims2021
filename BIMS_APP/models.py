from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Client(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    #phone number eqn
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')
    phone_Number = models.CharField(validators=[phone_number_validator], max_length=17, unique=True)
    Email = models.EmailField()
    Id_No = models.IntegerField(max_length=9,unique=True)
    DOB = models.DateField()


class Business(models.Model):
    Business_No = models.CharField(max_length=20)
    NameofBusiness = models.CharField(max_length=50,)
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)


