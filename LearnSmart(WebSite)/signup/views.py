from django.shortcuts import render, redirect
from .models import Register
from LearnSmart import views

# Create your views here.

def Register(request):
    data = {
        "title" : "LearnSmart | register",
        "css" : "/static/css/register.css",
        "js" : "/static/js/script.js",
    }
    
    try:
        if request.method == "POST":
        
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            print(fname, lname, email, password)
    except:
        print("Exception")
        pass
        
    return render(request, "register.html", data)
