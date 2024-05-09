from django.shortcuts import render


# Create your views here.

def Login(request):
    data = {
        "title" : "LearnSmart | login",
        "css" : "/static/css/loginStyle.css",
        "js" : "/static/js/script.js",
    }
    
    return render(request, "login.html", data)