from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30,primary_key = True)
    last_name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    def __str__(self):
        return self.first_name
    