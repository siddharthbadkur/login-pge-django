

from django.urls import path
from .views import home3

urlpatterns = [
    path('home/',home3,name='home3')
     

]