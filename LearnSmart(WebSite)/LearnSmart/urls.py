"""
URL configuration for LearnSmart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LearnSmart import views
from contact.views import contact
from signup.views import Register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('aboutus/', views.AboutUs, name="aboutus"),
    path('team/', views.Team, name="team"),
    path('services/', views.Services, name="services"),
    path('computer_courses/', views.ComputerCourses, name="computer_courses"),
    path('development_courses/', views.DevelopmentCourses, name="development_courses"),
    path('gate/', views.Gate, name="gate"),
    path('quiz/', views.Quiz, name="quiz"),
    path('login/', views.Login, name="login"),
    path('register/', Register, name="register"),
    path('contactus/', contact, name="contact"),
    path('feedback/', views.Feedback, name="feedback"),
]