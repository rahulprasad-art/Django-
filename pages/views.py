from urllib import response
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def homepageview(request):
    return HttpResponse("Hello Biatch")

