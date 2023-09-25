from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.

def homePageView(request,*args,**kwargs):
    context = {
        "Status":"Currently Working"
    }
    return render(request,"home.html",context)

def aboutMe(request,*args,**kwargs):
    
    return render(request,"about.html",{})

def contactPageView(*args,**kwargs):
    return HttpResponse('<h1>Contact Us At</h1>')

def checkPostsViews(request,*args,**kwarg):
    data = Posts.objects.all()
    # print(data.text)
    return render(request,"posts.html",{'data':data})
