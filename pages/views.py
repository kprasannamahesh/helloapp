from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request,*args,**kwargs):
    return render(request,"home.html",{})



def contactPageView(*args,**kwargs):
    return HttpResponse('<h1>Contact Us At</h1>')
