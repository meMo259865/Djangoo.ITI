from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Login(request):
    return HttpResponse('<h1>Hello from login</h1>')

def logout(request):
    return HttpResponse('<h1>Hello from logout</h1>')

def register(request):
    return HttpResponse('<h1>Hello from register</h1>')
