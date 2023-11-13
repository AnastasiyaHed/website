#модель, представляющая страница с полями
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

