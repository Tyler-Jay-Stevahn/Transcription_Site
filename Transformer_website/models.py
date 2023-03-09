from django.db import models
from django.utils import timezone
from django_pandas.managers import DataFrameManager

# Create your models here.
class database(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=25)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.author

class employees(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=25)
    description = models.TextField()
    pub_date = models.DateField(default=timezone.now())

    objects = DataFrameManager

    def __str__(self):
        return self.author

class registrationdata(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)