from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=30)
class Stocks(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25),
    symbol = models.CharField(max_length=20)
    shares = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()