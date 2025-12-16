from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField
    subject = models.CharField(max_length=100)
