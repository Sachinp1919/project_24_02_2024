from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=20)
    marks = models.FloatField()
    address = models.TextField()
