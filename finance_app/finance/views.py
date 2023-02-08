from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, 'finance/index.html')

def login(response):
    return render(response, 'finance/login.html')