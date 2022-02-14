from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from pymongo import MongoClient


# here I am 
# here  i am second 
# Create your views here.
def index(request):
    context = {
        "variable1":"Knowledge Platform is great",
        "variable2":"CDATA is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        ptype=request.POST['ptype']
        psummary=request.POST['psummary']
        pdescription=request.POST['pdescription']
        kanalysis=request.POST['kanalysis']
        kinsights=request.POST['kinsights']
        owner=request.POST['owner']
    
    
        conn = MongoClient()
        db=conn.users
        collection=db.knowledge
        rec1={"ptype":ptype,
          "psummary":psummary,
          "pdescription":pdescription,
          "kanalysis":kanalysis,
          "kinsights":kinsights,
          "owner":owner
        }
        collection.insert_one(rec1)
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


## login view
 
def index(request):
    print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")