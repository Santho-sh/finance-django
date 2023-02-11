from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    path("buy", views.buy, name= "buy"),
]
