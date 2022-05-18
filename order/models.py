from django.db import models
from main.models import Model

# Create your models here.
class Order(models.Model):
    products = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='orders')
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.email}'

