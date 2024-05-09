from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from contact.models import Contact
from signup.models import Register


def homePage(request):
    data = {
        "title" : "LearnSmart",
        "css" : "/static/css/style.css",
    }

    return render(request, "index.html", data)


def AboutUs(request):
    data = {
        "title" : "LearnSmart | about us",
        "css" : "/static/css/style.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "index.html", data)


def Team(request):
    data = {
        "title" : "LearnSmart | team",
        "css" : "/static/css/style.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "index.html", data)


def Services(request):
    data = {
        "title" : "LearnSmart | services",
        "css" : "/static/css/style.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "index.html", data)


def ComputerCourses(request):
    data = {
        "title" : "LearnSmart | computer courses",
        "css" : "/static/css/subjects.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "computer_courses.html", data)


def DevelopmentCourses(request):
    data = {
        "title" : "LearnSmart | development courses",
        "css" : "/static/css/subjects.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "development_courses.html", data)

 
def Gate(request):
    data = {
        "title" : "LearnSmart | gate",
        "css" : "/static/css/subjects.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "gate.html", data)


def Quiz(request):
    data = {
        "title" : "LearnSmart | quiz",
        "css" : "/static/css/quizStyle.css",
        "js" : "/static/js/script.js",
    }

    return render(request, "quiz.html", data)   


def Login(request):
    data = {
        "title" : "LearnSmart | login",
        "css" : "/static/css/loginStyle.css",
        "js" : "/static/js/script.js",
    }
    
    return render(request, "login.html", data)

'''
def Register(request):
    data = {
        "title" : "LearnSmart | register",
        "css" : "/static/css/register.css",
        "js" : "/static/js/script.js",
    }
    
    return render(request, "register.html", data)
'''


def Feedback(request):
    data = {
        "title" : "LearnSmart | feedback",
        "css" : "/static/css/style.css",
        "js" : "/static/js/script.js",
    }

    try:
        if request.method == 'GET':
            name = request.GET.get['your_name']
            email = request.GET.get['email']
            msg = request.GET.get['additional']
            
            print(name, email, msg)
            url = "/"
            return redirect(url)
    except:
        print("Exception")
        pass

    return render(request, "index.html", data)
