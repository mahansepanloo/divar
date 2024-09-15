from django.db import models
from django.contrib.auth.models import User
from prodact.models import Product

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prodict = models.ForeignKey(Product, on_delete=models.CharField)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
