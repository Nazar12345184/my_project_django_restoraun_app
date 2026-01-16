from django.db import models

class menuu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=False)
    icon = models.ImageField(upload_to="static/images/")

class com(models.Model):
    name = models.ForeignKey(menuu, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)

# Create your models here.
