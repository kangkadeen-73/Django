from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

app_name = "accountapp"

def hello_world(request):
    return HttpResponse('Hello world!')


