from django.urls import path
from . import views

urlpatterns =[
 # Home page of this app
 path("",views.index,name="index"),
 # what comes after / it gives us different https reponse
 path("miku",views.miku,name="miku"),
 path("<str:name>",views.greet,name="greet")
 ]