from django.shortcuts import render
from .models import Admin


def homepage(request):
    return render(request,"index.html")
def loginpage(request):
    return render(request,"login.html")
def contactpage(request):
    return render(request,"contact.html")
def aboutpage(request):
    return render(request,"about.html")

def checkadminlogin(request):
    if request.method=="POST":
        adminuname=request.POST["uname"]
        adminpwd=request.POST["pwd"]
        flag=Admin.objects.filter(username=adminuname,password=adminpwd).values()
        if flag:
            return render(request,"ttmhome.html")
        else:
            return render(request,"loginfail.html")