from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='images', default='Screenshot_from_2023-01-07_20-45-18.png')

