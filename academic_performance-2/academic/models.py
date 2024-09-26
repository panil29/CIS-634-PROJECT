from django.db import models

# Create your models here.
class Adminlogin(models.Model):
    
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):

        return self.username[:50]

class AddFaculty_Model(models.Model):
    fullname=models.CharField(max_length=40)
    email=models.EmailField(blank=False,unique=True)
    password=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    subject=models.CharField(max_length=10)
    state=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    addr=models.TextField(default='DataFlair Address')
    
    def __str__(self):

        return self.fullname

class AddStudent_Model(models.Model):

    rollno=models.CharField(max_length=20)
    fullname=models.CharField(max_length=40)
    email=models.EmailField(blank=False,unique=True)
    password=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    year=models.CharField(max_length=15)
    state=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    addr=models.TextField(default='DataFlair Address')
    
    def __str__(self):

        return self.rollno

class Internal_Model(models.Model):

    rollno=models.ForeignKey(AddStudent_Model,on_delete=models.CASCADE)

    cns=models.IntegerField()

    uml=models.IntegerField()

    mc=models.IntegerField()

    stm=models.IntegerField()

    hbd=models.IntegerField()

    attendance=models.IntegerField()

    
