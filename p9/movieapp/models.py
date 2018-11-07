from django.db import models

class movie(models.Model):
    rdate=models.DateField()
    mname=models.CharField(max_length=200)
    hero=models.CharField(max_length=100)
    heroine=models.CharField(max_length=100)
    rating=models.IntegerField()

