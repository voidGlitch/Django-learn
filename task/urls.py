from django.urls import path
from . import views

urlpatterns =[
 # Home page of this app
 path("",views.index,name="index"),
 ]