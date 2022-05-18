from django.db import models



CHOICES = (
    ('in stock', 'В наличии'),
    ('out of stock', 'Нет в наличии')
)
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='Brand')

    def __str__(self):
        return f'{self.name}'


class Model(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='models')
    status = models.CharField(choices=CHOICES, max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')

    def __str__(self):
        return self.title



