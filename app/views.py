from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Hai(request):
    return HttpResponse('This is my Hai View')