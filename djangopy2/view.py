#from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    conntext = {}
    conntext['hello'] = 'Hello World!'
    return render(request,'hello.html',conntext)