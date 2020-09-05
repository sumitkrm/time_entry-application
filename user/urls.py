from django.urls import path, include 
from django.conf import settings 
from . import views 
from django.conf.urls.static import static 
  
urlpatterns = [ 
         path('', views.index, name ='index'),
         path('time_chart', views.time_chart, name = 'time_chart')
]