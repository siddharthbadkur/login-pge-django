
from django.urls import path
from .views import home2

urlpatterns = [
    path('home/',home2,name='home2')
     

]