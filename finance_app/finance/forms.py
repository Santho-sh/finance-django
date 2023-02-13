from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class BuyForm(forms.Form):
    symbol = forms.CharField(label='Symbol', max_length=15)
    shares = forms.IntegerField()
    
class QuoteForm(forms.Form):
    symbol = forms.CharField(label='Symbol', max_length=15)