from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        verbose_name='Product Name',
        help_text='Product name should be less than 100 characters',
        null=True,
        blank=True
    )
    price = models.FloatField(
        verbose_name='Product Price',
        null=True,
        blank=True
    )
    stock = models.IntegerField(
        verbose_name='Product Stock',
        help_text='Product stock should be a non-negative integer',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Product"