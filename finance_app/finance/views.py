from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Stocks
# Create your views here.

def index(response):
    stocks = Stocks.objects.all()
    return render(response, 'finance/index.html', {'stocks':stocks})

def login(response):
    return render(response, 'finance/login.html')