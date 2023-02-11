from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='person', null=True)
    name = models.CharField(max_length=30)
    balance = models.FloatField()
    
    def __str__(self):
        return self.name
class Stocks(models.Model):
    user_id = models.ForeignKey(Person,on_delete=models.CASCADE)
    company = models.CharField(max_length=25)
    symbol = models.CharField(max_length=20)
    shares = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
