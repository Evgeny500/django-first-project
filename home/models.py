from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    passwordRepeat = models.CharField(max_length=50)