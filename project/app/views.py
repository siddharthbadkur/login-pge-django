from django.shortcuts import render
from django.http   import HttpResponse, JsonResponse 

# Create your views here.
# def home(request):
#     data={'name':'siddharth',"course":"python full stack "
#     }
#     return JsonResponse (data)
def register(request):
    return render(request,'register.html')