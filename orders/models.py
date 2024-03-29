from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + str(self.amount) + " " + str(self.date)


class Product(models.Model):
    order = models.ManyToManyField(Order)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + " " + self.description

