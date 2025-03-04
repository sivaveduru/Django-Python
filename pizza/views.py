from django.shortcuts import render

# Create your views here.
from .models import Pizza

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza/home.html', {'pizzas': pizzas})
