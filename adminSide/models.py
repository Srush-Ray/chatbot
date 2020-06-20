from django.db import models

# Create your models here.
class qa(models.Model):
    question=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)


class admin(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=10)