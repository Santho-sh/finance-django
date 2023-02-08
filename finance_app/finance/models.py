from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.CharField(max_length=30)
    balance = models.FloatField()
class Stocks(models.Model):
    user_id = models.ForeignKey(Person,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=20)
    shares = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
