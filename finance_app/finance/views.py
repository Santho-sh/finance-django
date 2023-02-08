from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Stocks
from .forms import SignUpForm
# Create your views here.

def index(response):
    stocks = Stocks.objects.all()
    return render(response, 'finance/index.html', {'stocks':stocks})

def signup(response):
    if response.method == 'POST':
        form = SignUpForm(response.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = SignUpForm()
    return render(response, 'finance/signup.html', {'form': form})