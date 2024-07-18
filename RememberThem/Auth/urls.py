from django.urls import path
from . import views

urlpatterns = [
    path("",views.LogIn,name=""),
    path("registration/",views.Registration,name=""),
]