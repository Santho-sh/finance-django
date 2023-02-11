from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Person, Stocks


def index(response):
    
    stocks = Stocks.objects.filter(user_id=response.user.id)

    return render(response, 'finance/index.html', {'stocks':stocks})

def register(response):
    
    if response.method == 'POST':
        
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            user = form.save()
            
            Person.objects.create(name=response.user.username, balance=10000.0)
            
            login(response, user)
            messages.success(response, "Registration successful." )
                  
            return redirect('/')
        
        messages.error(response, "Unsuccessful registration. Invalid information.")
    
    form = RegisterForm()
    return render(response, 'finance/register.html', {'form': form})


def login_request(response):
    
    if response.method == 'POST':
        
        form = AuthenticationForm(response, data=response.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(response, user)
                messages.info(response, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(response, "Invalid username or password.")
        else:
            messages.error(response, "Invalid username or password.")
            
    form = AuthenticationForm()    
    return render(response, 'registration/login.html', {'form':form})


def logout_request(response):
    logout(response)
    return redirect("/")