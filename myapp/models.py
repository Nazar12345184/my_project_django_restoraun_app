from django.db import models

class menuu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=False)
    icon = models.ImageField(upload_to="static/images/")

# Create your models here.
