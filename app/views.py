from django.shortcuts import render
from app.views import *
# Create your views here.


def parent(request):
    return render(request,'parent.html')


def child(request):
    return render(request,'child.html')
    