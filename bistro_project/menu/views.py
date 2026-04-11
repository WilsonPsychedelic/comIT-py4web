from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish

def menu_view(request):
    items = Dish.objects.all()

    return render(request, 'menu.html', {'menu_items': items})

def home():
    bistro = "<h1>My Cool Bistro</h1>"
    return HttpResponse(bistro)
