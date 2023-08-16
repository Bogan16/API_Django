from django.db import models

class DeliveryCrew(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):
    delivery_crew = models.ForeignKey(DeliveryCrew, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)

class Cart(models.Model):
    items = models.ManyToManyField(MenuItem)
