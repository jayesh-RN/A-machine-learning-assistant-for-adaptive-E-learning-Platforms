from django.db import models
    
# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    msg=models.TextField(max_length=100)
    additional=models.TextField(max_length=200)
    
    def _str_(self):
        return self.fname + " " + self.email


