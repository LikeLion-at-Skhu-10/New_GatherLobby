from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def signin_searchid(request):
    return render(request, "signin_searchid.html")

def signin_searchpw(request):
    return render(request, "signin_searchpw.html")