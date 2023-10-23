# from django.shortcuts import render
from .models import Place
from django.shortcuts import render

def index(request):
    obj = Place.objects.all()
    # obj2 = Place2.objects.all()
    return render(request, "index.html",{'result': obj})
def commerce(request):
    return render(request, 'commerce.html')
def computer(request):
    return render(request, 'computer.html')
def science(request):
    return render(request, 'science.html')
def english(request):
    return render(request, 'english.html')
def malayalam(request):
    return render(request, 'malayalam.html')
def hindi(request):
    return render(request, 'hindi.html')