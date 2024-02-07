from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    context = {
        'carousel' : HeaderText.objects.all()
    }
    return render(request, 'index.html', context)

def About(request):
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Contact(request):
    return render(request, 'contact.html')

def Furniture(request):
    return render(request, 'furniture.html')
