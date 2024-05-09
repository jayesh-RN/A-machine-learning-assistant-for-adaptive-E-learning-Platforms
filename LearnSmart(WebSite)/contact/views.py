from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):
    data = {
        "title" : "LearnSmart | contactus",
        "css" : "/static/css/contact.css",
    }
    try:
        if request.method == 'POST':
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            msg = request.POST.get('message')
            additional = request.POST.get('additional')
            print(fname, lname, email, msg, additional)
            
            en = Contact(fname=fname, lname=lname, email=email, msg=msg, additional=additional)
            
            try:
                en.save()
                print("Data saved successfully")            
            except Exception as e:
                print("Error: ", e)
                print("Data not saved")
        else:
            print("Method not post")
    except Exception as e:
        print("Error: ", e)

    return render(request, "contact.html", data)