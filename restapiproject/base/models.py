from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100, null=True)
    price  =models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)