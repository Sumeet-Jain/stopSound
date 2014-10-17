from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def denied(request):
    return render(request, 'base/access_denied.html')
