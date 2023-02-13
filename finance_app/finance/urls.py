from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path("logout/", views.logout_request, name= "logout"),
    path("password_change/", views.password_change_request, name= "password_change"),
    path("buy/", views.buy, name= "buy"),
    path("quote/", views.quote, name= "quote"),
    path("add/", views.add, name= "add"),
    path("sell/", views.sell, name= "sell"),
]