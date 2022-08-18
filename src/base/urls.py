from django.urls import path
from . import views

urlpatterns = [
  path('api/adduser', views.adduser),
  path('api/getuser/<str:username>', views.getuser),
  path('api/getallusers', views.getallusers)
]