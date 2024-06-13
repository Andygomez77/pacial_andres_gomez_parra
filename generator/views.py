from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Carro

def about(request):
    #return HttpResponse ('hello world')
    car = Carro.objects.all()
    return render(request, 'generator/about.html', {'cars':car})

def home(request):
    return render(request, 'generator/home.html')

def models(request):
    cars = Carro.objects.all().order_by('-precio')
    return render(request, 'generator/modelos.html', {'cars':cars})

def models_info(request, carro_id):
    car = get_object_or_404(Carro, pk = carro_id)
    return render(request, 'generator/info.html', {'carro':car})

