from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return  HttpResponse("PFSD SDP Project")

def demofunction1(request):
    return  HttpResponse("<h3>KL University</h3>")

def demofunction2(request):
    return  HttpResponse("<font color ='green'>Learning Management System</font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    return HttpResponse(adminuname,adminpwd)

