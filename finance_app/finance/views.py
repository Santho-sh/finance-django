from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages
from .models import Person, Stocks


def index(response):
    
    if response.method == 'POST':
        stocks = Stocks.objects.all()
        return render(response, 'finance/index.html', {'stocks':stocks})
    else:
        return redirect('login/')

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            user = form.save()
            login(response, user)
            messages.success(response, "Registration successful.")
            return redirect('finance:home')
        
        messages.error(response, "Unsuccessful registration. Invalid information.")
    
    form = RegisterForm()
    return render(response, 'finance/register.html', {'form': form})