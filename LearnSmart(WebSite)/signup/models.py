from django.db import models

# Create your models here.
class Register(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    
    def _str_(self):
        return self.fname + " " + self.email