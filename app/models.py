from django.db import models

# Create your models here.
class Info(models.Model):
    Name=models.CharField(max_length=90,default="")
    Age=models.CharField(max_length=90,default="")
    Notes=models.CharField(max_length=90,default="")
