from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .models import Person, Stocks
from .forms import RegisterForm, BuyForm, QuoteForm, AddCashForm
from .helpers import lookup, usd

from django.contrib.auth import get_user_model
User = get_user_model()

def index(response):
    
    stocks = Stocks.objects.filter(user_id=response.user.id).values()
    
    total = 0
    
    for i in range(len(stocks)):
        total += stocks[i]['total']
    
    user = Person.objects.filter(user_id=response.user.id).values('balance')
                
    balance = user[0]['balance']
    
    total += balance
    
    return render(response, 'finance/index.html', {'stocks':stocks, 'balance':balance, 'total':total})

def register(response):
    
    if response.method == 'POST':
        
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            user = form.save()
            login(response, user)
            
            name = response.user.username
            id = response.user.id
            print(name, id)
            Person.objects.create(user_id=user, name=name.title(), balance=10000.0)
            
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


def password_change_request(response):
    User = get_user_model()
    if response.method == 'POST':
        ...
    form = PasswordChangeForm(user=User)
    return render(response, 'registration/password_change.html', {'form':form})
    


def buy(response):
    if response.method == 'POST':
        form = BuyForm(response.POST)
        if form.is_valid():
            symbol = form.cleaned_data.get('symbol')
            shares = form.cleaned_data.get('shares')
            quote = lookup(symbol)
            
            if quote != None or shares < 1:
                
                user = Person.objects.filter(user_id=response.user.id).values('balance')
                
                balance = user[0]['balance']
                print()
                
                price = quote['price']
                name = quote['name']
                total_price = price * shares
                
                if total_price < balance:
                    ...
                else:
                    return redirect('/buy')
            else:
                return redirect('/buy')
    else:
        form = BuyForm()
        return render(response, "finance/buy.html", {'form':form})


def sell(response):
    if response.method == 'POST':
        form = response.POST
        if form.is_valid():
            symbol = form.cleaned_data.get('symbol')
            stocks = form.cleaned_data.get('stocks')
            print(symbol, stocks)
    else:
        stocks = Stocks.objects.filter(user_id=response.user.id).values()

    return render(response, 'finance/sell.html', {'stocks': stocks})

def quote(response):
    if response.method == 'POST':
        form = QuoteForm(response.POST)
        
        if form.is_valid():
            
            symbol = form.cleaned_data.get('symbol')
            data = lookup(symbol)
            if data != None:
                
                price = data['price']
                name = data['name']
                context = {'name':name, 'price':price, 'symbol':symbol}
                return render(response, 'finance/quoted.html', context)
            
            else:
                return redirect('/quote')
    else:
        form = QuoteForm()
        return render(response, 'finance/quote.html', {'form':form})

def add(response):
    if response.method == 'POST':
        form = AddCashForm(response.POST)
        if form.is_valid():
            cash = form.cleaned_data.get('cash')
            print(cash)
        else:
            return redirect('/add')
    else: 
        form = AddCashForm()
    return render(response, 'finance/add.html', {'form': form})