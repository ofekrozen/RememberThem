from django.shortcuts import render

# Create your views here.

def LogIn(request):
    return render(request, 'Auth/login.html')

def Register(request):
    return render(request,"Auth/register.html")