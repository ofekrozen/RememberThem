from django.urls import path
from . import views

urlpatterns = [
    path("",views.LogIn,name=""),
    path("register/",views.Register,name=""),
]