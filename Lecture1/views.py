from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
 #This is used to create a httpresponse to start an app
 # return HttpResponse("Hello World") 
 #render a particular file on the screen
 return render(request,"hello/index.html")

def miku(request):
 return HttpResponse("Hi bro")

#function to greet someone by taking there name is the url
def greet (request,name):
 return HttpResponse(f"hello {name.capitalize()}")