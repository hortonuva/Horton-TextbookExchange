from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Sherriff! You're at the textbook exchange index.  Cool test!  Yes it is!")
