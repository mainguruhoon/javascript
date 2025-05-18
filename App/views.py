from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(req):
    return render(req, 'login.html')

def loginuser(req):
    username=req.POST.get("username")
    password=req.POST.get("password")

    if username == "admin" and password == "admin123":
        return HttpResponse("login success")
    else:
        return HttpResponse("invalid data")
