from django.shortcuts import render
from django.http import HttpResponse

def background(request):
    return render(request, 'template/background.html')