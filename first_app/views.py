from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse("This is contact page!")

def about(request):
    return HttpResponse("This is about page!")