from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


# client model
class Client(models.Model):
    Acc_No = models.CharField(max_length=40,default=True)   # MEL/2021/1
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)

    #phonenumber expression
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')
    Phone_Number = models.CharField(validators=[phone_number_validator], max_length=17, unique=True)
    PoBox = models.IntegerField(default=True)
    Residence = models.CharField(max_length=60,default=True)
    Email = models.EmailField()
    Id_No = models.IntegerField(unique=True,default=True)
    DOB = models.DateField(auto_now_add=True)
    Occupation = models.CharField(max_length=40,default=True)


# group model
class Group(models.Model):
    NameOfTheGroup = models.CharField(max_length=50,unique=True)
    ChairOfGroup = models.CharField(max_length=50)
    Treasurer = models.CharField(max_length=50)
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')
    TPNumber = models.CharField(validators=[phone_number_validator],max_length=17,unique=True)
    YOE = models.DateField(auto_now_add=True)


#loans creation model
class Loans(models.Model):
    Loan_Name = models.CharField(max_length=99)
    Loan_Duration = models.DecimalField(max_digits=7,decimal_places=2)
    Amount = models.IntegerField()
    CratedOn = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=True)


# loans application model
class Application(models.Model):
    ClientName = models.ForeignKey(Client,on_delete=models.CASCADE)
    Loan = models.ForeignKey(Loans,on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)
    AppliedOn = models.DateField(auto_now_add=True)
    TimeDue = models.DateField(auto_now_add=True)


