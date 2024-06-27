

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home2(request):
    return HttpResponse('welcome to  app 2  home2 page')
