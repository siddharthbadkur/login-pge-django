
from django.urls import path
from .views import home1

urlpatterns = [
    path('home/',home1,name='home1')
     

]