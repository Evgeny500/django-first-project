from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import User

# Create your views here.

def create(request):
    if request.method == "POST":
        user = User()
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.passwordRepeat = request.POST.get("passwordRepeat")
        user.save()
    return HttpResponseRedirect("/")

def home(request):
    return render(request, 'home/home.html', {'title': 'Главная мой первый сайт на Django'})

def page1(request):
    return render(request, 'home/home.html', {'title': 'Страница 1'})

def page2(request):
    return render(request, 'home/home.html', {'title': 'Страница 2'})