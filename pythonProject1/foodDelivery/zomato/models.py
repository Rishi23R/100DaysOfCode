from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    city = models.CharField(max_length=200)
    offer = models.BooleanField()


class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
