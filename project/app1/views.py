from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(request):
    return HttpResponse('welcome to  app 1  home1 page')
